import React, {Component, PropTypes} from 'react'
import {observable} from 'mobx'
import MyComponent from './MyComponent'
import Options from './Options'
import Nav from './Nav'
import Backendless from 'backendless'

const options = observable([
  {branch: 'master', description: 'Minimal setup - mobx react webpack'},
  {branch: 'less', description: 'With Less for CSS'},
  {branch: 'react-router', description: 'With React Router'}
])

Backendless.enablePromises()

export default class App extends Component {

  constructor (props) {
    super(props)
    this.state = {
      users: []
    }
  }

  componentDidMount () {
    this.getUsers()
  }

  setNewState (data) {
    console.log('*** setNewState data: ', data)
    this.setState({
      users: data
    })
    console.log('*** setNewState setState state.users: ', this.state.users)
  }

  getUsers () {
    let userRegistered = (users) => {
      console.log('user has registered: ', users)
      this.setNewState(users.data)
    }
    let gotError = (err) => {
      console.log('error message - ' + err.message)
      console.log('error code - ' + err.statusCode)
    }
    Backendless.Persistence.of(Backendless.User).find()
      .then(userRegistered)
      .catch(gotError)
  }

  registerUser (e) {
    e.preventDefault()
    const email = e.target.email.value
    const password = e.target.password.value
    var user = new Backendless.User()
    user.email = email
    user.password = password
    Backendless.UserService.register(user)
      .then(data => this.getUsers())
      .catch(console.log('**** sorry :('))
  }

  render () {
    const { users } = this.state
    console.log('**** users in state: ', users)
    if (!users) {
      return <h1>...Loading</h1>
    }
    return (
      <div className="container">
        <h1>React • Mobx • Webpack</h1>
        <hr/>
        <div className="row">
          <div>
            <h2>Пользователи ({users.length}):</h2>
            <ul>
              {this.state.users.map(user => <li key={user.objectId}>{user.email}</li>)}
            </ul>
          </div>
          <div className="col-sm-6">
            <form onSubmit={this.registerUser.bind(this)}>
              <input type="email" placeholder="email" name="email" />
              <input type="password" placeholder="пароль" name="password" />
              <button type="submit">Зарегистрироваться</button>
            </form>
          </div>
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
