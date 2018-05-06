import React, { Component } from 'react';
import './Cover.css';
import coverImg from './images/cover.jpg';

export default class Cover extends Component {
  render() {
    return (
      <div className="cover">
        <div className="cover-img" style={{ backgroundImage: `url(${coverImg})` }} />
      </div>
    );
  }
}
