import React, {Component} from 'react'
import {Redirect, Route, Switch} from 'react-router-dom'
import { Layout } from 'antd'

import memoryUtils from '../../utils/memoryUtils'
import storageUtils from '../../utils/storageUtils'
import LeftNav from '../../components/left-nav'
import Header from '../../components/header'
import Home from '../home/home'
import Category from '../category/category'
import Product from '../product/product'
import Role from '../role/role'
import User from '../user/user'
import NotFound from '../not-found/not-found'


const { Footer, Sider, Content } = Layout

/*
后台管理的路由组件
 */
export default class Admin extends Component {
  render () {
    const user = memoryUtils.user
    let timeStamp = Date.parse(new Date()) / 1000
    console.log('expires at ' + user.expires + '. current timestamp is ' + timeStamp)
    // 如果内存没有存储user ==> 当前没有登陆
    if(!user || !user._id || user.expires <= timeStamp) {
      // 自动跳转到登陆(在render()中)
      storageUtils.removeUser()
      memoryUtils.user = {}
      return <Redirect to='/login'/>
    }
    return (
      <Layout style={{minHeight: '100%'}}>
        <Sider>
          <LeftNav/>
        </Sider>
        <Layout>
          <Header>Header</Header>
          <Content style={{margin: 20, backgroundColor: '#fff'}}>
            <Switch>
              <Redirect from='/' exact to='/home'/>
              <Route path='/home' component={Home}/>
              <Route path='/category' component={Category}/>
              <Route path='/product' component={Product}/>
              <Route path='/user' component={User}/>
              <Route path='/role' component={Role}/>
              <Route component={NotFound}/>
            </Switch>
          </Content>
          <Footer style={{textAlign: 'center', color: '#cccccc'}}>推荐使用谷歌浏览器|开发者: WuYang|email: wuyangwebdeveloper@163.com|技术架构：React+Flask</Footer>
        </Layout>
      </Layout>
    )
  }
}