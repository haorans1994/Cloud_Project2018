import React, { Component } from 'react';
import { ScenarioSittingChart, ScenarioSittingBar } from '../Chart';

export default class Sitting extends Component {
  render() {
    return (
      <div>
        <ScenarioSittingChart />
        <ScenarioSittingBar />
      </div>
    );
  }
}
