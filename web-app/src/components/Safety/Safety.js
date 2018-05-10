import React, { Component, Fragment } from 'react';
import axios from 'axios';
import ScenarioSafetyChart from './components/ScenarioSafetyChart';
import dataChartJson from './data/data_chart.json';

const URL = 'http://127.0.0.1:5984/tweets_mel/66ade9406878ad62924e7baf03a5d2a2';
// const URL = 'http://115.146.86.192:5984/tweets_mel/66ade9406878ad62924e7baf03a5d2a2';

export default class Safety extends Component {
  state = {
    chartData: null
  };

  componentDidMount() {
    this.fetchData(URL);
  }

  fetchData = async url => {
    let dataTotal = null;
    try {
      const res = await axios.get(url, {
        headers: {
          'content-type': 'application/json'
        }
      });
      dataTotal = res.data.data.data;
    } catch (err) {
      dataTotal = dataChartJson;
    }
    const safetyData = Object.values(dataTotal);
    const dataDayTime = safetyData
      .filter(item => Array.isArray(item))
      .map(item => ({ positive: item[8] * 100, safety: item[5] }));
    const dataNightTime = safetyData
      .filter(item => Array.isArray(item))
      .map(item => ({ positive: item[8] * 100, safety: item[6] }));
    const chartData = { DayTime: dataDayTime, NightTime: dataNightTime };
    this.setState({ chartData });
  };

  render() {
    const { chartData } = this.state;
    return (
      <Fragment>
        <div className="intro">
          <div className="title">Perception of safety just has little affect on sentiment</div>
          <div className="description">
            {`From the graph, we can know that, people have higher safety rate in one suburb during day time. But the other side it shows that the result regarding the positive rate for the high safety rate does not match with our prediction. We used to assume that those suburb with higher positive rate will have higher safety rate. However, the results show that there has no particular obvious link between them. This means that people's emotions do not affect their sense of security, or, it is not a decisive factor.`}
          </div>
        </div>
        {chartData && <ScenarioSafetyChart data={chartData} />}
      </Fragment>
    );
  }
}
