import React, { Component, Fragment } from 'react';
import ScenarioCityChart from './components/ScenarioCityChart';
import dataChartJson from './data/data_chart.json';

export default class City extends Component {
  render() {
    return (
      <Fragment>
        <div className="intro">
          <div className="title">Different cities have various characteristics</div>
          <div className="description">
            {`For different cities, there might be different cultures, so people might use different words. For example, those people who live near the equatorial may post more word such as “hot” etc. For those cities that are relatively close to the university, their high-frequency words may be "libraries". We grab the coordinates from the tweets we captured and then classify them into different cities. Count the tweets issued in each city to obtain high-frequency words for different cities.`}
          </div>
        </div>
        <ScenarioCityChart data={dataChartJson} />;
      </Fragment>
    );
  }
}
