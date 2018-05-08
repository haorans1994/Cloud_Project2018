import React, { Component } from 'react';
import { ScenarioWeatherWindChart } from '../Chart';
import { ScenarioWeatherRainChart } from '../Chart';

export default class Weather extends Component {
  render() {
    return (
      <div>
        <ScenarioWeatherWindChart />
        <ScenarioWeatherRainChart />
      </div>
    );
  }
}
