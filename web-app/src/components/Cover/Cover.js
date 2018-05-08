import React, { Component } from 'react';
import './Cover.css';
import coverImg from './images/cover3.jpg';

export default class Cover extends Component {
  render() {
    return (
      <div className="cover">
        <div className="cover-img" style={{ backgroundImage: `url(${coverImg})` }}>
          <div className="cover-title">
            COMP90024<br />
            Cloud<br />
            Assignment 2
          </div>
        </div>
      </div>
    );
  }
}
