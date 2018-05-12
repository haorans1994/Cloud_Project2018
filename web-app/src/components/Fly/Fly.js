import React, { Component } from 'react';

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
    if (window.matchMedia('(min-width: 768px)').matches) {
      const { speed } = this.props;
      let factor = 5;
      if (speed === 'slow') {
        factor = 8;
      } else if (speed === 'fast') {
        factor = 3;
      }
      let { flyHeight } = this.state;
      const top =
        this.fly.current.getBoundingClientRect().top + this.fly.current.firstChild.offsetTop;
      const height = this.fly.current.firstChild.clientHeight;
      if (top <= window.innerHeight && top >= -height) {
        flyHeight = (window.innerHeight - top) / factor;
      }
      this.setState({ flyHeight });
    }
  };

  render() {
    const { children } = this.props;
    const { flyHeight } = this.state;
    return (
      <div
        ref={this.fly}
        style={{
          position: 'relative',
          willChange: 'transform',
          transform: `translateY(-${flyHeight}px)`
        }}
      >
        {children}
      </div>
    );
  }
}
