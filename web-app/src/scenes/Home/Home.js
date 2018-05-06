import React, { Component } from 'react';
import Cover from '../../components/Cover/Cover';
import ScenarioList from '../../components/ScenarioList/ScenarioList';
import './Home.css';
import teamImg from './images/team.jpg';

export default class Home extends Component {
  render() {
    return (
      <div className="home">
        <Cover />
        <h1 className="title">Scenarios</h1>
        <ScenarioList />
        <h1 className="title">Team</h1>
        <div className="team">
          <div className="team-img" style={{ backgroundImage: `url(${teamImg}）` }} />
        </div>
      </div>
    );
  }
}
