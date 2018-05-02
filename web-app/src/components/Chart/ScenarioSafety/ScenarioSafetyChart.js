import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ReactEcharts from 'echarts-for-react';
import dataChart from './data/data_chart.json';

export default class ScenarioSafetyChart extends Component {
  static propTypes = {
    height: PropTypes.number
  };

  static defaultProps = {
    height: 500
  };

  render() {
    const { height } = this.props;
    const dataMale = dataChart.male.map(obj => [obj.positive, obj.safety]);
    const dataFemale = dataChart.female.map(obj => [obj.positive, obj.safety]);
    const options = {
      title: {
        text: 'Safety',
        subtext: 'data from json file',
        left: 'center'
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
            return `${params.seriesName} :<br/>${params.value[0]}cm ${params.value[1]}kg `;
          }
          return `${params.seriesName} :<br/>${params.name} : ${params.value}kg `;
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
        data: ['女性', '男性'],
        left: 'center'
      },
      xAxis: [
        {
          type: 'value',
          scale: true,
          axisLabel: {
            formatter: '{value} cm'
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
            formatter: '{value} kg'
          },
          splitLine: {
            show: false
          }
        }
      ],
      series: [
        {
          name: '女性',
          type: 'scatter',
          data: dataFemale,
          itemStyle: {
            color: '#f1c400'
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
                  name: '女性分布区间',
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
            data: [{ type: 'max', name: '最大值' }, { type: 'min', name: '最小值' }]
          },
          markLine: {
            lineStyle: {
              normal: {
                type: 'solid'
              }
            },
            data: [{ type: 'average', name: '平均值' }, { xAxis: 160 }]
          }
        },
        {
          name: '男性',
          type: 'scatter',
          data: dataMale,
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
                  name: '男性分布区间',
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
            data: [{ type: 'max', name: '最大值' }, { type: 'min', name: '最小值' }]
          },
          markLine: {
            lineStyle: {
              normal: {
                type: 'solid'
              }
            },
            data: [{ type: 'average', name: '平均值' }, { xAxis: 170 }]
          }
        }
      ]
    };

    return <ReactEcharts option={options} notMerge lazyUpdate style={{ height: `${height}px` }} />;
  }
}
