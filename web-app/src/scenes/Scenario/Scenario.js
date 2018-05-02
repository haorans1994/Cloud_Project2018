import React, { Component } from 'react';
import { Route } from 'react-router-dom';
import ScenarioSafetyChart from '../../components/Chart/ScenarioSafety/ScenarioSafetyChart';

export default class Scenario extends Component {
  render() {
    const { match } = this.props;
    return (
      <div>
        <h1>Scenario Page</h1>
        <Route path={`${match.url}/sitting`} component={ScenarioSafetyChart} />
      </div>
    );
  }
}
