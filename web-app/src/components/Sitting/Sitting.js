import React, { Component, Fragment } from 'react';
import axios from 'axios';
import { ScenarioSittingScatter } from '../Chart';

const URL = 'http://127.0.0.1:5984/tweets_mel/66ade9406878ad62924e7baf03a5d2a2';

export default class Sitting extends Component {
  state = {
    chartData: null
  };
  componentDidMount() {
    this.fetchData(URL);
  }

  fetchData = url => {
    axios
      .get(url, {
        headers: {
          'content-type': 'application/json'
        }
      })
      .then(res => {
        const dataTotal = res.data.data.data;
        const sittingDataTotal = Object.values(dataTotal);
        const sittingData = sittingDataTotal
          .filter(item => Array.isArray(item))
          .map(item => ({ positive: item[8] * 100, sitting: item[7] }));

        const sittingCount = sittingDataTotal
          .filter(item => Array.isArray(item))
          .map(item => ({ LGAcode: item[3], count: item[9] }));
        const chartData = { Sitting: sittingData };
        const barData = [sittingCount];
        console.log(chartData);
        console.log(barData);
        this.setState({ chartData, barData });
      })
      .catch(err => {
        console.error(err);
      });
  };

  render() {
    const { chartData } = this.state;
    return (
      <Fragment>
        <div className="intro">
          <div className="title">Long-period sitting can cause a negative impact for person</div>
          <div className="description">
            {`From the chart, we can get a trend: the greater the percentage of people who spend an average of more than seven hours sitting, the less positive rate on Twitter in the area. The reason for this may be that the time spent sitting is due to work. People with long working hours are more likely to send negative tweets, which cause the low positive rate.`}
          </div>
        </div>
        <ScenarioSittingScatter data={chartData} />
        {/* <ScenarioSittingBar data={barData} /> */}
      </Fragment>
    );
  }
}
