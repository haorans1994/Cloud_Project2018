import React, { Component } from 'react';
import './Fly.css';

export default class Fly extends Component {
  constructor() {
    super();
    this.state = {
      flyHeight: 0
    };
    this.fly = React.createRef();
  }

  componentDidMount() {
    document.addEventListener('scroll', this.onScroll);
  }

  componentWillUnmount() {
    document.removeEventListener('scroll', this.onScroll);
  }

  onScroll = () => {
    const height = this.fly.current.firstChild.clientHeight;
    const top = this.fly.current.offsetTop;
    let flyHeight = 0;
    if (window.scrollY >= top - window.innerHeight && window.scrollY < top + height) {
      console.log(top, height, window.scrollY);
      flyHeight = -(window.scrollY - (top - window.innerHeight)) / 4;
      console.log(flyHeight);
    }
    this.setState({ flyHeight });
  };

  render() {
    const { children } = this.props;
    const { flyHeight } = this.state;
    return (
      <div
        ref={this.fly}
        className="fly"
        style={{ willChange: 'transform', transform: `translateY(${flyHeight}px)` }}
      >
        {children}
      </div>
    );
  }
}
