import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ReactEcharts from 'echarts-for-react';

export default class ScenarioWeatherWindChart extends Component {
  static propTypes = {
    height: PropTypes.number
  };

  static defaultProps = {
    height: 400
  };

  render() {
    const { height, data } = this.props;
    const colors = ['#5793f3', '#d14a61', '#675bba'];
    const options = {
      color: colors,
      tooltip: {
        trigger: 'none',
        axisPointer: {
          type: 'cross'
        }
      },
      legend: {
        data: ['Rain', 'Positive Rate']
      },
      grid: {
        top: 70,
        bottom: 50
      },
      xAxis: [
        {
          type: 'category',
          axisTick: {
            alignWithLabel: true
          },
          axisLine: {
            onZero: false,
            lineStyle: {
              color: colors[1]
            }
          },
          axisPointer: {
            label: {
              formatter: params =>
                `Positive${params.value}${
                  params.seriesData.length ? `：${params.seriesData[0].data}` : ''
                }`
            }
          },
          data: [
            '2018/4/24',
            '2018/4/25',
            '2018/4/26',
            '2018/4/27',
            '2018/4/28',
            '2018/4/29',
            '2018/4/30'
          ]
        },
        {
          type: 'category',
          axisTick: {
            alignWithLabel: true
          },
          axisLine: {
            onZero: false,
            lineStyle: {
              color: colors[0]
            }
          },
          axisPointer: {
            label: {
              formatter: params =>
                `Positive${params.value}${
                  params.seriesData.length ? `：${params.seriesData[0].data}` : ''
                }`
            }
          }
        }
      ],
      yAxis: [
        {
          type: 'value'
        }
      ],
      series: [
        {
          name: 'Rain',
          type: 'line',
          xAxisIndex: 1,
          smooth: true,
          data: [0, 0, 0, 0.6, 6.2, 0.8, 11]
        },
        {
          name: 'Positive Rate',
          type: 'line',
          smooth: true,
          data: data.positive
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
