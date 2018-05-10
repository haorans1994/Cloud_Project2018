import React, { Component } from 'react';
import Cover from '../../components/Cover/Cover';
import ScenarioList from '../../components/ScenarioList/ScenarioList';
import Fly from '../../components/Fly/Fly';
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
          <div className="team-img" style={{ backgroundImage: `url(${teamImg})` }} />
          <div className="team-overlay">
            <div className="name" style={{ top: '50%', left: '10%' }}>
              <Fly>
                <div>Niu Tong</div>
                <div className="student-id">811179</div>
              </Fly>
            </div>
            <div className="name" style={{ top: '53%', left: '22%' }}>
              <Fly>
                <div>Yunpeng Shao</div>
                <div className="student-id">854611</div>
              </Fly>
            </div>
            <div className="name" style={{ top: '63%', left: '49%' }}>
              <Fly>
                <div>
                  Qingqian
                  <div className="surname">Yang</div>
                  <div className="student-id">736563</div>
                </div>
              </Fly>
            </div>
            <div className="name" style={{ top: '60%', left: '64%' }}>
              <Fly>
                <div>Fei Teng</div>
                <div className="student-id">809370</div>
              </Fly>
            </div>
            <div className="name" style={{ top: '55%', left: '83%' }}>
              <Fly>
                <div>Haoran Sun</div>
                <div className="student-id">839693</div>
              </Fly>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
