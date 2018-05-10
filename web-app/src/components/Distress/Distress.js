import React, { Component, Fragment } from 'react';
import axios from 'axios';
import ScenarioDistressChart from './components/ScenarioDistressChart';
import dataChartJson from './data/data_chart.json';

const URL = 'http://127.0.0.1:5984/distress_rate/66ade9406878ad62924e7baf03a5aa62';
// const URL = 'http://115.146.86.192:5984/distress_rate/66ade9406878ad62924e7baf03a5aa62';

export default class Distress extends Component {
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
      dataTotal = res.data.data;
    } catch (err) {
      dataTotal = dataChartJson;
    }
    const perthData = Object.values(dataTotal.perth);
    const dataPerthChart = perthData
      .filter(item => Array.isArray(item))
      .map(item => ({ positive: item[5] * 100, distress: item[4] }));

    const sydData = Object.values(dataTotal.sydney);
    const dataSydChart = sydData
      .filter(item => Array.isArray(item))
      .map(item => ({ positive: item[5] * 100, distress: item[4] }));

    const melData = Object.values(dataTotal.melbourne);
    const dataMelChart = melData
      .filter(item => Array.isArray(item))
      .map(item => ({ positive: item[5] * 100, distress: item[4] }));
    const chartData = { Mel: dataMelChart, Syd: dataSydChart, Perth: dataPerthChart };

    this.setState({ chartData });
  };

  render() {
    const { chartData } = this.state;
    return (
      <Fragment>
        <div className="intro">
          <div className="title">
            Psychological Distress symptom can effect individuals&apos; sentiment
          </div>
          <div className="description">
            {`From the results, we can easily see that those areas with low positive rates have higher psychological distress rate. This result is in line with our expectations. It is worth pointing out that Perth has a wider range of positive rates because the range of its psychological distress rate is the narrowest of the three cities.`}
          </div>
        </div>
        {chartData && <ScenarioDistressChart data={chartData} height={800} />}
      </Fragment>
    );
  }
}
