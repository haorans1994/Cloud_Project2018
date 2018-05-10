import React, { Component } from 'react';
import ScenarioWeatherWindChart from './components/ScenarioWeatherWindChart';
import ScenarioWeatherRainChart from './components/ScenarioWeatherRainChart';
import dataWindChartJson from './data/data_wind_chart.json';
import dataRainChartJson from './data/data_rain_chart.json';

export default class Weather extends Component {
  render() {
    return (
      <div>
        <ScenarioWeatherWindChart data={dataWindChartJson} />
        <ScenarioWeatherRainChart data={dataRainChartJson} />
      </div>
    );
  }
}
