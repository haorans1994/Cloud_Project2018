import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ReactEcharts from 'echarts-for-react';
import dataChart from './data/data_chart.json';

export default class ScenarioCityChart extends Component {
  static propTypes = {
    height: PropTypes.number
  };

  static defaultProps = {
    height: 600
  };

  render() {
    const { height } = this.props;
    const data = dataChart;
    const options = {
      tooltip: {
        trigger: 'item',
        triggerOn: 'mousemove'
      },
      series: [
        {
          type: 'tree',
          data: [data],
          top: '1%',
          left: '7%',
          bottom: '1%',
          right: '20%',

          symbolSize: 8,

          label: {
            normal: {
              position: 'left',
              verticalAlign: 'middle',
              align: 'right',
              fontSize: 15
            }
          },

          leaves: {
            label: {
              normal: {
                position: 'right',
                verticalAlign: 'middle',
                align: 'left'
              }
            }
          },

          expandAndCollapse: true,
          animationDuration: 550,
          animationDurationUpdate: 750
        }
      ]
    };
    return (
      <ReactEcharts
        option={options}
        notMerge
        lazyUpdate
        className="chart"
        style={{ height: `${height}px` }}
      />
    );
  }
}
