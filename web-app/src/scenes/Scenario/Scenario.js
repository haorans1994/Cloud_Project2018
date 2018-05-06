import React, { Component } from 'react';
import { Route, Link } from 'react-router-dom';

import Safety from '../../components/Safety/Safety';
import { ScenarioDistressChart } from '../../components/Chart';
import './Scenario.css';

export default class Scenario extends Component {
  render() {
    const { match } = this.props;
    return (
      <div className="scenario">
        <Link to="/">Home</Link>
        <div className="scenario-container">
          <Route path={`${match.url}/safety`} component={Safety} />
          <Route path={`${match.url}/distress`} component={ScenarioDistressChart} />
        </div>
      </div>
    );
  }
}
