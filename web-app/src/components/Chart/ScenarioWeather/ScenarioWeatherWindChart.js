import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ReactEcharts from 'echarts-for-react';
import dataChart from './data/data_wind_chart.json';

export default class ScenarioWeatherWindChart extends Component {
  static propTypes = {
    height: PropTypes.number
  };

  static defaultProps = {
    height: 400
  };

  render() {
    const { height } = this.props;
    const data = dataChart.positive;
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
        data: ['2015 降水量', '2016 降水量']
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
                `降水量${params.value}${
                  params.seriesData.length ? `：${params.seriesData[0].data}` : ''
                }`
            }
          },
          data: ['2016-1', '2016-2', '2016-3', '2016-4', '2016-5', '2016-6', '2016-7']
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
                `降水量${params.value}${
                  params.seriesData.length ? `：${params.seriesData[0].data}` : ''
                }`
            }
          },
          data: ['2015-1', '2015-2', '2015-3', '2015-4', '2015-5', '2015-6', '2015-7']
        }
      ],
      yAxis: [
        {
          type: 'value'
        }
      ],
      series: [
        {
          name: '2015 降水量',
          type: 'line',
          xAxisIndex: 1,
          smooth: true,
          data: [22, 24, 37, 70, 30, 22]
        },
        {
          name: '2016 降水量',
          type: 'line',
          smooth: true,
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
