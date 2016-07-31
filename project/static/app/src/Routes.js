import React, {Component} from 'react'
import { Router, Route, browserHistory } from 'react-router'
import App from './App'
import Page1 from './App/Page1'
import Page2 from './App/Page2'
import Page2SubComponent from './App/Page2/Page2SubComponent'

export default class Routes extends Component {
  render () {
    return (
      <Router history={browserHistory}>
        <Route path="/" component={App}>
          <Route path="page1" component={Page1}/>
          <Route path="page2" component={Page2}>
            <Route path=":id" component={Page2SubComponent} />
          </Route>
        </Route>
      </Router>
    )
  }
}

Routes.propTypes = {

}

Routes.defaultProps = {

}
