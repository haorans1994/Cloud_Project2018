import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ReactEcharts from 'echarts-for-react';

export default class ScenarioDistressChart extends Component {
  static propTypes = {
    height: PropTypes.number
  };
  static defaultProps = {
    height: 600
  };

  render() {
    const { height, data } = this.props;
    const dataMel = data.Mel.map(obj => [obj.positive, obj.distress]);
    const dataSyd = data.Syd.map(obj => [obj.positive, obj.distress]);
    const dataPerth = data.Perth.map(obj => [obj.positive, obj.distress]);

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
      // toolbox: {
      //   feature: {
      //     dataZoom: {},
      //     brush: {
      //       type: ['rect', 'polygon', 'clear']
      //     }
      //   }
      // },
      // brush: {},
      legend: {
        data: ['Melbourne', 'Sydney', 'Perth'],
        left: 'center'
      },
      xAxis: [
        {
          name: 'Positive Rate',
          nameGap: 27,
          nameLocation: 'center',
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
          name: 'Distress Rate',
          nameLocation: 'center',
          nameGap: 50,
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
          }
        },
        {
          name: 'Perth',
          type: 'scatter',
          data: dataPerth,
          itemStyle: {
            color: '#003399'
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
