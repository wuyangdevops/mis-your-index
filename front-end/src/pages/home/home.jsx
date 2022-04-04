import React, {Component} from 'react'
import {
  Icon,
  Card,
  Statistic,
  // DatePicker,
  Timeline
} from 'antd'
// import moment from 'moment'

import Line from './line'
import Bar from './bar'
import './home.less'
import memoryUtils from '../../utils/memoryUtils'
import { reqTaskList, reqOverviewData, reqVisitorSales, reqCurveData } from '../../api'
// import Item from 'antd/lib/list/Item'

// const dateFormat = 'YYYY/MM/DD'
// const {RangePicker} = DatePicker

export default class Home extends Component {

  state = {
    // loading: false, // 是否正在获取数据中
    overviewLoading: false,
    overviewDetails: {
      'count': 0, // 商品总数
      'week': 0,  // 周同比
      'day': 0, // 日同比
      'weekDirection': 'arrow-down', // 周同比箭头方向
      'dayDirection': 'arrow-down', // 日同比箭头方向
      'weekColor': '#3f8600', // 周同比箭头颜色
      'dayColor': '#3f8600' // 日同比箭头颜色
    },
    graphLoading: false,  // graph是否在获取数据
    graphData: [],  // 销量/访问图数据
    lineData: [], // 曲线图数据
    isVisited: true,
    taskList: []
  }

  handleChange = (isVisited, change) => {
    return () => {
    if (change === true) {  
      this.setState({isVisited})
    }
    this.getVisitorSales(isVisited)}
  }

  componentDidMount () {
    console.log('++req to task api++')
    this.getPlan()
    console.log('++req to overview data api++')
    this.getOverviewData()
    console.log('++req to graph data api++')
    this.getVisitorSales()
    console.log('++req to line data api++')
    this.getLineData()
  }

  // line
  getLineData = async () => {
    const {data, status} = await reqCurveData()
    if (status === 0){
      this.setState({lineData: data})
    }
  }

  // graph
  getVisitorSales = async (isVisited) => {
    this.setState({graphLoading: true})
    const {data, status} = await reqVisitorSales(isVisited)
    if (status === 0){
      this.setState({graphData: data})
    }
    this.setState({graphLoading: false})
  }

  getOverviewData = async () => {
    // 请求总览api
    this.setState({overviewLoading: true})
    const {data, status} = await reqOverviewData()
    if (status === 0){
        let count = data.count
        let week = data.week
        let weekDirection = 'arrow-down'
        let weekColor = '#3f8600'
        if (week >= 0) {
          weekDirection = 'arrow-up'
          weekColor = 'red'
        }
        let day = data.day
        let dayDirection = 'arrow-down'
        let dayColor = '#3f8600'
        if (day >= 0){
          dayDirection = 'arrow-up'
          dayColor = 'red'
        }
        week = Math.abs(week)
        day = Math.abs(day)
        console.log('++after abs, week is ' + week)
        let overviewDetails = {
          count,
          week,
          weekDirection,
          weekColor,
          day,
          dayDirection,
          dayColor
        }
        this.setState({overviewDetails})
    }
    this.setState({overviewLoading: false})
  }

  getCommodityOverview = () => {
    console.log('overview detail: week: ' + this.state.overviewDetails.week)

    return (
        <Card
        className="home-card"
        title="商品总量"
        // extra={<Icon style={{color: 'rgba(0,0,0,.45)'}} type="question-circle"/>}
        style={{width: 250}}
        headStyle={{color: 'rgba(0,0,0,.45)'}}
        loading={this.state.overviewLoading}
      >
        <Statistic
          value={this.state.overviewDetails.count}
          suffix="个"
          style={{fontWeight: 'bolder'}}
        />
        <Statistic
          value={this.state.overviewDetails.week}
          valueStyle={{fontSize: 15}}
          prefix={'周同比'}
          suffix={<div>%<Icon style={{color: this.state.overviewDetails.weekColor, marginLeft: 10}} 
          type={this.state.overviewDetails.weekDirection}/></div>}
        />
        <Statistic
          value={this.state.overviewDetails.day}
          valueStyle={{fontSize: 15}}
          prefix={'日同比'}
          suffix={<div>%<Icon style={{color: this.state.overviewDetails.dayColor, marginLeft: 10}} 
          type={this.state.overviewDetails.dayDirection}/></div>}
        />
      </Card>
    )
  }

  getPlan = async () => {
    const username = memoryUtils.user.username
    // console.log('username: ' + username)
    const res = await reqTaskList(username)
    // console.log('api res is ' + res.status)
    const tasks = res.data
    let taskList = []
    // console.log('++task data length: ' + tasks.length)
    for (let index=0; index < tasks.length; index++){
      let s = tasks[index].status
      let c = tasks[index].context
      let color = 'green'
      if (s === '0') {
        color = 'red'
      }
      taskList.push({'color': color, 'context': c})
      // console.log('color: ' + color + ', context: ' + c)
    }
    // console.log('taskList length is: ' + taskList.length)
    this.setState({taskList})
  }

  listTask = () => {
    let tmp = this.state.taskList
    const planList = Array.from(tmp)
    // console.log('++planList length is: ' + planList.length)
    return (
    <Timeline>
      {
        planList.map((item, index) => {
          // console.log('color: ' + item.color + 'context: ' + item.context)
          return <Timeline.Item color={item.color} key={index}>{item.context}</Timeline.Item>
        })
      }
    </Timeline>)
  }


  render() {
    
    const {isVisited} = this.state
    return (
      <div className='home'>
          {this.getCommodityOverview()}

        <Line lineData={this.state.lineData}/>

        <Card
          className="home-content"
          title={<div className="home-menu">
            <span className={isVisited ? "home-menu-active home-menu-visited" : 'home-menu-visited'}
                  onClick={this.handleChange(true, true)}>访问量</span>
            <span className={isVisited ? "" : 'home-menu-active'} onClick={this.handleChange(false, true)}>销售量</span>
          </div>}
          // extra={<RangePicker
          //   defaultValue={[moment('2022/01/01', dateFormat), moment('2022/03/01', dateFormat)]}
          //   format={dateFormat}
          // />}
        >
          <Card
            className="home-table-left"
            title={isVisited ? '访问趋势' : '销售趋势'}
            bodyStyle={{padding: 0, height: 275}}
            loading={this.state.graphLoading}
            extra={<Icon type="reload" onClick={this.handleChange(isVisited, false)}/>}
          >
            <Bar graphData={this.state.graphData}/>
          </Card>
          <Card title='任务' className="home-table-right" extra={<Icon type="reload" onClick={this.getPlan}/>}>
            {this.listTask()}
          </Card>
        </Card>
      </div>
    )
  }
}