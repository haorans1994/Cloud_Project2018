import mpi4py.MPI as MPI
from itertools import islice
import re
from textblob import TextBlob
import emoji

# This function is to count the total line for the instagram file
def countLine(path):
    num = 0
    f = open(path, 'r')
    while True:
        buffer = f.read(102400)
        if not buffer:
            break
        num += buffer.count('\n') # calculate the num of \n to check the num of line
    f.close()
    return num

def judge_sentiment(start_line, block_line, file):
    sentimentResult = {}
    f = open(file, 'r')
    current_line = 0
    for line in islice(f, start_line, None):
        if current_line < block_line:
            if "text\":\"" in line:
                temp1 = re.findall(r"text\":\"(.*)\"created_at\":\"", line)
                temp2 = re.findall(r"(.*)\",\"created_at\":\"", temp1[0])  #cut the "created_at" part again because it appear twice in line
                temp3 = emoji.demojize(temp2[0])
                text = temp3.lower()  # to lower case
                text = re.sub(r'[@][\S]*\s', 'TAG', text)  # replace the @user with tag
                text = re.sub(r'((www\.[^\s]+)|(https?://[^\s]+))', 'URL', text)  # replace the web address with url
                text = re.sub(r'#([^\s]+)', r'\1', text)  # remove the '#'
                text = re.sub('_', ' ', text)  # remove the '_'
                text = re.sub(':', ' ', text)  # remove the ':'
                text = re.sub('[\s]+', ' ', text)  # remove the duplicate space
                correct = TextBlob(text).correct()  # correct the text spell error
                sentiment = correct.sentiment
                if sentiment[0] < 0:
                    tag = 'negative'
                elif sentiment[0] > 0:
                    tag = 'positive'
                else:
                    tag = 'neutral'
                sentimentResult[temp2[0]] = tag
            current_line += 1
        else:
            break
    f.close()
    return sentimentResult

comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()
if comm_rank == 0:
    file = "tweets_crawler2.json"
    line_size = countLine(file)
    # get the size for the block_line according to the number of the total processes
    if line_size % comm_size:
        block_line = line_size // comm_size + 1
    else:
        block_line = line_size // comm_size

# broadcast the block_line, file path to all
block_line = comm.bcast(block_line if comm_rank == 0else None, root=0)
file = comm.bcast(file if comm_rank == 0else None, root=0)
# all ranks will do this function to get the result
result = judge_sentiment(comm_rank*block_line, block_line, file)

# gather the results from all ranks and process the result by adding all the items of each result and get the final sentiment dict
results = comm.gather(result, root=0)
if comm_rank == 0:
    i = 0
    final_result = {}
    for result in results:
        for k, v in result.items():
                final_result[k] = v