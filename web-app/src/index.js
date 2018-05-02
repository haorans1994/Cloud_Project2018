import React, { Fragment } from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Home from './scenes/Home/Home';
import Scenario from './scenes/Scenario/Scenario';
import registerServiceWorker from './registerServiceWorker';
import './index.css';

ReactDOM.render(
  <Router>
    <Fragment>
      <Route path="/" exact component={Home} />
      <Route path="/scenario" component={Scenario} />
    </Fragment>
  </Router>,
  document.getElementById('root')
);
registerServiceWorker();
