import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ReactEcharts from 'echarts-for-react';
import dataChartJson from './data/data_scatter.json';

export default class ScenarioSittingChart extends Component {
  static propTypes = {
    height: PropTypes.number
  };

  static defaultProps = {
    height: 600
  };

  render() {
    const { height, data } = this.props;
    const dataChart = data || dataChartJson;
    const dataSitting = dataChart.Sitting.map(obj => [obj.positive, obj.sitting]);
    console.log(dataSitting);
    const options = {
      title: {
        text: 'Sitting Rate',
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
        data: ['Sitting over 7 hours per day'],
        left: 'center'
      },
      xAxis: [
        {
          name: 'Positive Rate',
          nameGap: '25',
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
          name: 'Sitting Rate',
          nameLocation: 'center',
          nameGap: 55,
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
          name: 'Sitting Over 7 Hours per Day',
          type: 'scatter',
          data: dataSitting,
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
                  name: 'Sitting Rate Distribution',
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
        // {
        //   name: 'DayTime',
        //   type: 'scatter',
        //   data: dataSitting,
        //   markArea: {
        //     silent: true,
        //     itemStyle: {
        //       normal: {
        //         color: 'transparent',
        //         borderWidth: 1,
        //         borderType: 'dashed'
        //       }
        //     },
        //     data: [
        //       [
        //         {
        //           name: 'DayTime Distribution',
        //           xAxis: 'min',
        //           yAxis: 'min'
        //         },
        //         {
        //           xAxis: 'max',
        //           yAxis: 'max'
        //         }
        //       ]
        //     ]
        //   },
        //   markPoint: {
        //     data: [{ type: 'max', name: 'Maximum' }, { type: 'min', name: 'minimum' }]
        //   }
        // }
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
