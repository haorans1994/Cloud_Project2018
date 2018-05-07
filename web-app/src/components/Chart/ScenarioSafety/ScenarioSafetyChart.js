import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ReactEcharts from 'echarts-for-react';
import dataChart from './data/data_chart.json';

export default class ScenarioSafetyChart extends Component {
  static propTypes = {
    height: PropTypes.number
  };

  static defaultProps = {
    height: 600
  };

  render() {
    const { height } = this.props;
    const dataDay = dataChart.DayTime.map(obj => [obj.positive, obj.safety]);
    const dataNight = dataChart.NightTime.map(obj => [obj.positive, obj.safety]);
    const options = {
      title: {
        text: 'Safety Rate',
        subtext: 'Consistency with Positive Rate'
      },
      grid: {
        left: '3%',
        right: '7%',
        bottom: '3%',
        containLabel: true
      },
      tooltip: {
        // trigger: 'axis',
        showDelay: 0,
        formatter: params => {
          if (params.value.length > 1) {
            return `${params.seriesName} :<br/>${params.value[0]}% ${params.value[1]}% `;
          }
          return `${params.seriesName} :<br/>${params.name} : ${params.value}% `;
        },
        axisPointer: {
          show: true,
          type: 'cross',
          lineStyle: {
            type: 'dashed',
            width: 1
          }
        }
      },
      toolbox: {
        feature: {
          dataZoom: {},
          brush: {
            type: ['rect', 'polygon', 'clear']
          }
        }
      },
      brush: {},
      legend: {
        data: ['NightTime', 'DayTime'],
        left: 'center'
      },
      xAxis: [
        {
          type: 'value',
          scale: true,
          axisLabel: {
            formatter: '{value} %'
          },
          splitLine: {
            show: false
          }
        }
      ],
      yAxis: [
        {
          type: 'value',
          scale: true,
          axisLabel: {
            formatter: '{value} %'
          },
          splitLine: {
            show: false
          }
        }
      ],
      series: [
        {
          name: 'NightTime',
          type: 'scatter',
          data: dataNight,
          itemStyle: {
            color: '#333333'
          },
          markArea: {
            silent: true,
            itemStyle: {
              normal: {
                color: 'transparent',
                borderWidth: 1,
                borderType: 'dashed'
              }
            },
            data: [
              [
                {
                  name: 'NightTime Distribution',
                  xAxis: 'min',
                  yAxis: 'min'
                },
                {
                  xAxis: 'max',
                  yAxis: 'max'
                }
              ]
            ]
          },
          markPoint: {
            data: [{ type: 'max', name: 'Maximum' }, { type: 'min', name: 'Minimum' }]
          }
        },
        {
          name: 'DayTime',
          type: 'scatter',
          data: dataDay,
          markArea: {
            silent: true,
            itemStyle: {
              normal: {
                color: 'transparent',
                borderWidth: 1,
                borderType: 'dashed'
              }
            },
            data: [
              [
                {
                  name: 'DayTime Distribution',
                  xAxis: 'min',
                  yAxis: 'min'
                },
                {
                  xAxis: 'max',
                  yAxis: 'max'
                }
              ]
            ]
          },
          markPoint: {
            data: [{ type: 'max', name: 'Maximum' }, { type: 'min', name: 'minimum' }]
          }
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
