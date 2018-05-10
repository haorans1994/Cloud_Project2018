import React, { Component, Fragment } from 'react';
import axios from 'axios';
import { ScenarioSafetyChart } from '../Chart';

const URL = 'http://127.0.0.1:5984/tweets_mel/66ade9406878ad62924e7baf03a5d2a2';

export default class Safety extends Component {
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
        const safetyData = Object.values(dataTotal);
        const dataDayTime = safetyData
          .filter(item => Array.isArray(item))
          .map(item => ({ positive: item[8] * 100, safety: item[5] }));
        const dataNightTime = safetyData
          .filter(item => Array.isArray(item))
          .map(item => ({ positive: item[8] * 100, safety: item[6] }));
        const chartData = { DayTime: dataDayTime, NightTime: dataNightTime };
        console.log(chartData);
        this.setState({ chartData });
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
          <div className="title">Perception of safety just has little affect on sentiment</div>
          <div className="description">
            {`From the graph, we can know that, people have higher safety rate in one suburb during day time. But the other side it shows that the result regarding the positive rate for the high safety rate does not match with our prediction. We used to assume that those suburb with higher positive rate will have higher safety rate. However, the results show that there has no particular obvious link between them. This means that people's emotions do not affect their sense of security, or, it is not a decisive factor.`}
          </div>
        </div>
        <ScenarioSafetyChart data={chartData} />
      </Fragment>
    );
  }
}
