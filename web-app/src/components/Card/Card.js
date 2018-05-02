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
      opacity: 0
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
    const cardHeight = this.card.current.offsetHeight;
    const cardTop = this.card.current.offsetTop;
    let opacity = 0.1;
    if (
      window.scrollY >= cardTop - window.innerHeight &&
      window.scrollY < cardTop - window.innerHeight + cardHeight
    ) {
      opacity = Math.min(1, (window.innerHeight + window.scrollY - cardTop) / cardHeight + 0.1);
    } else if (
      window.scrollY >= cardTop - window.innerHeight + cardHeight &&
      window.scrollY < cardTop + 70
    ) {
      opacity = 1;
    } else if (window.scrollY >= cardTop + 70 && window.scrollY < cardTop + cardHeight) {
      opacity = (cardHeight + cardTop + 70 - window.scrollY) / cardHeight;
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
