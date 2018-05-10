import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import Card from '../Card/Card';
import Fly from '../Fly/Fly';
import './ScenarioList.css';
import imgScenarioSitting from './images/scenario_sitting.jpg';
import imgScenarioDistress from './images/scenario_distress.jpg';
import imgScenarioSafety from './images/scenario_safety.jpg';
import imgScenarioWeather from './images/scenario_weather.jpg';
import imgScenarioSydmel from './images/scenario_sydmel.jpg';

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
          <Fly speed="slow">
            <Card
              image={imgScenarioSafety}
              title="Safety"
              titlePosition="top"
              className="second-scenario"
            />
          </Fly>
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
          <Fly>
            <Card
              image={imgScenarioWeather}
              title="Weather"
              titlePosition="top"
              className="fourth-scenario"
            />
          </Fly>
        </Link>
        <Link to="/scenario/city">
          <Fly speed="fast">
            <Card
              image={imgScenarioSydmel}
              title="AUS-City"
              titlePosition="right"
              className="fifth-scenario"
            />
          </Fly>
        </Link>
      </div>
    );
  }
}
