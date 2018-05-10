import React, { Component } from 'react';
import { Route, Link } from 'react-router-dom';

import Safety from '../../components/Safety/Safety';
import Distress from '../../components/Distress/Distress';
import Sitting from '../../components/Sitting/Sitting';
import Weather from '../../components/Weather/Weather';
import City from '../../components/City/City';
import './Scenario.css';

export default class Scenario extends Component {
  componentDidMount() {
    window.scroll(0, 0);
  }

  render() {
    const { match } = this.props;
    return (
      <div className="scenario">
        <Link to="/" className="home-btn">
          Home
        </Link>
        <div className="scenario-container">
          <Route path={`${match.url}/safety`} component={Safety} />
          <Route path={`${match.url}/distress`} component={Distress} />
          <Route path={`${match.url}/sitting`} component={Sitting} />
          <Route path={`${match.url}/weather`} component={Weather} />
          <Route path={`${match.url}/city`} component={City} />
        </div>
      </div>
    );
  }
}
