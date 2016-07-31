import React, {Component, PropTypes} from 'react'
import {observable} from 'mobx'
import MyComponent from './MyComponent'
import Options from './Options'
import Nav from './Nav'

const options = observable([
  {branch: 'master', description: 'Minimal setup - mobx react webpack'},
  {branch: 'less', description: 'With Less for CSS'},
  {branch: 'react-router', description: 'With React Router'}
])

export default class App extends Component {
  render () {
    return (
      <div className="container">
        <h1>React • Mobx 123 • Webpack</h1>
        <hr/>
        <div className="row">
          <div className="col-sm-6">
            <Nav />
            <h2>Options</h2>
            <Options options={options}/>
            <MyComponent />
          </div>
          <div className="col-sm-6">
            {this.props.children}
          </div>
        </div>
      </div>
    )
  }
}

App.propTypes = {
  children: PropTypes.node
}
