import React, { Component } from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import './Card.css';

export default class Card extends Component {
  static propTypes = {
    image: PropTypes.string,
    title: PropTypes.string,
    className: PropTypes.string
  };

  static defaultProps = {
    image: null,
    title: null,
    className: null
  };

  constructor() {
    super();
    this.state = {
      opacity: 0.1
    };
    this.card = React.createRef();
  }

  componentDidMount() {
    document.addEventListener('scroll', this.onScroll);
  }

  componentWillUnmount() {
    document.removeEventListener('scroll', this.onScroll);
  }

  onScroll = () => {
    let { opacity } = this.state;
    const { top } = this.card.current.getBoundingClientRect();
    const height = this.card.current.offsetHeight;
    if (top < window.innerHeight && top >= window.innerHeight - height) {
      opacity = Math.min(1, (window.innerHeight - top) / height + 0.1);
    } else if (top < window.innerHeight - height && top >= 0) {
      opacity = 1;
    } else if (top < 0 && top >= -height) {
      opacity = Math.min(1, (top + height) / height + 0.1);
    } else {
      opacity = 0;
    }
    this.setState({ opacity });
  };

  render() {
    const { image, title, className } = this.props;
    const { opacity } = this.state;
    return (
      <div
        ref={this.card}
        className={classNames('card', className)}
        style={{ willChange: 'opacity', opacity }}
      >
        <div className="card-title">{title}</div>
        <div className="card-img-container">
          <div className="card-img-ghost" />
          <div className="card-img" style={{ backgroundImage: `url(${image})` }} />
        </div>
      </div>
    );
  }
}
