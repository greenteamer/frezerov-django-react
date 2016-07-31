import React, {Component, PropTypes} from 'react'

export default class Page2 extends Component {
  render () {
    return (
      <div>
        <h3>Page2</h3>
        {this.props.children}
      </div>
    )
  }
}

Page2.propTypes = {
  children: PropTypes.node
}

Page2.defaultProps = {

}
