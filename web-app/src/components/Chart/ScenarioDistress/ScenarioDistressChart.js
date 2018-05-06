import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ReactEcharts from 'echarts-for-react';
import dataChart from './data/data_chart.json';

export default class ScenarioDistressChart extends Component {
  static propTypes = {
    height: PropTypes.number
  };
  static defaultProps = {
    height: 600
  };

  render() {
    const { height } = this.props;
    const dataMel = dataChart.Mel.map(obj => [obj.positive, obj.distress]);
    const dataSyd = dataChart.Syd.map(obj => [obj.positive, obj.distress]);
    const dataPerth = dataChart.Perth.map(obj => [obj.positive, obj.distress]);

    const options = {
      title: {
        text: 'Psychological Distress Rate',
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
        data: ['Melbourne', 'Sydney'],
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
          name: 'Melbourne',
          type: 'scatter',
          data: dataMel,
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
                  name: 'Melbourne Distribution',
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
          },
          markLine: {
            lineStyle: {
              normal: {
                type: 'solid'
              }
            },
            data: [{ type: 'average', name: 'Average' }, { xAxis: 160 }]
          }
        },
        {
          name: 'Sydney',
          type: 'scatter',
          data: dataSyd,
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
                  name: 'Sydney Distribution',
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
          },
          markLine: {
            lineStyle: {
              normal: {
                type: 'solid'
              }
            },
            data: [{ type: 'average', name: 'Average' }, { xAxis: 170 }]
          }
        },
        {
          name: 'Perth',
          type: 'scatter',
          data: dataPerth,
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
                  name: 'Perth Distribution',
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
          },
          markLine: {
            lineStyle: {
              normal: {
                type: 'solid'
              }
            },
            data: [{ type: 'average', name: 'Average' }, { xAxis: 160 }]
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