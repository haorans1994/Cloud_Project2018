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
        data: ['Max Wind Gust', 'Positive Rate']
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
          data: ['2018/5/1', '2018/5/2', '2018/5/3', '2018/5/4', '2018/5/5', '2018/5/6', '2018/5/7']
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
          name: 'Max Wind Gust',
          type: 'line',
          xAxisIndex: 1,
          smooth: true,
          data: [22, 24, 37, 70, 30, 22, 41]
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
