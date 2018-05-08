import React, { Component, Fragment } from 'react';
import axios from 'axios';
import { ScenarioSafetyChart } from '../Chart';

export default class Safety extends Component {
  state = {
    chartData: null
  };

  componentDidMount() {
    this.fetchData();
  }

  fetchData = () => {
    const url =
      'http://127.0.0.1:5984/tweets_crawler/_design/tweets_crawler/_view/melbourne_tweets';
    axios
      .get(url)
      .then(res => {
        console.log(res);
        const chartData = res.data;
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
          <div className="title">Safety</div>
          <div className="description">
            {`There are two slightly different meanings of safety. For example, home safety may
            indicate a building's ability to protect against external harm events (such as weather,
            home invasion, etc.), or may indicate that its internal installations (such as
            appliances, stairs, etc.) are safe (not dangerous or harmful) for its inhabitants.`}
          </div>
        </div>
        <ScenarioSafetyChart data={chartData} />
      </Fragment>
    );
  }
}
