import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ReactEcharts from 'echarts-for-react';
import echarts from 'echarts';
import dataBar from './data/data_bar.json';

export default class ScenarioSittingBar extends Component {
  static propTypes = {
    height: PropTypes.number
  };

  static defaultProps = {
    height: 600
  };

  render() {
    const sortedData = dataBar.sort((a, b) => b.count - a.count);
    const data = sortedData.map(obj => obj.count);
    const dataAxis = sortedData.map(obj => obj.postcode);
    const { height } = this.props;
    const options = {
      title: {
        text: 'The Number of Twitters in Each Suburb'
      },
      xAxis: {
        data: dataAxis,
        axisLabel: {
          rotate: 60,
          bottom: true,
          textStyle: {
            color: '#000000'
          }
        },
        axisTick: {
          show: false
        },
        axisLine: {
          show: false
        },
        z: 10
      },
      yAxis: {
        axisLine: {
          show: false
        },
        axisTick: {
          show: false
        },
        axisLabel: {
          textStyle: {
            color: '#999'
          }
        }
      },
      dataZoom: [
        {
          type: 'inside'
        }
      ],
      series: [
        {
          // For shadow
          type: 'bar',
          itemStyle: {
            normal: { color: 'rgba(0,0,0,0.05)' }
          },
          barGap: '-100%',
          barCategoryGap: '40%',
          // data: dataShadow,
          animation: false
        },
        {
          type: 'bar',
          itemStyle: {
            normal: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                { offset: 0, color: '#83bff6' },
                { offset: 0.5, color: '#188df0' },
                { offset: 1, color: '#188df0' }
              ])
            },
            emphasis: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                { offset: 0, color: '#2378f7' },
                { offset: 0.7, color: '#2378f7' },
                { offset: 1, color: '#83bff6' }
              ])
            }
          },
          data
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
