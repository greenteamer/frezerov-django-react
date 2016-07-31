import React, {Component} from 'react'
import {Link} from 'react-router'

export default class Nav extends Component {
  render () {
    return (
      <div>
        <h3>Navigation</h3>
        <ul className="list-inline">
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/page1">Page1</Link>
          </li>
          <li>
            <Link to="/page2">Page2</Link>
          </li>
          <li>
            <Link to="/page2/someId">Page2: someId</Link>
          </li>
        </ul>
      </div>
    )
  }
}

Nav.propTypes = {

}

Nav.defaultProps = {

}
