import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import Card from '../Card/Card';
// import Fly from '../Fly/Fly';
import './ScenarioList.css';
import imgScenarioSitting from './images/scenario_sitting.jpg';
import imgScenarioDistress from './images/scenario_distress.jpg';
import imgScenarioSafety from './images/scenario_safety.jpg';

export default class ScenarioList extends Component {
  render() {
    return (
      <div className="scenario-list">
        <Link to="/scenario/sitting">
          <Card
            image={imgScenarioSitting}
            title="Sitting"
            titlePosition="right"
            className="first-scenario"
          />
        </Link>
        <Link to="/scenario/safety">
          <Card
            image={imgScenarioSafety}
            title="Safety"
            titlePosition="top"
            className="second-scenario"
          />
        </Link>
        <Link to="/scenario/distress">
          <Card
            image={imgScenarioDistress}
            title="Distress"
            titlePosition="bottom"
            className="third-scenario"
          />
        </Link>
        <Link to="/scenario/weather">
          <Card
            image={imgScenarioSitting}
            title="Weather"
            titlePosition="right"
            className="fourth-scenario"
          />
        </Link>
      </div>
    );
  }
}
