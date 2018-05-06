import React, { Component, Fragment } from 'react';
import { ScenarioSafetyChart } from '../Chart';

export default class Safety extends Component {
  render() {
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
        <ScenarioSafetyChart />
      </Fragment>
    );
  }
}
