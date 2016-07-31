import React, {Component, PropTypes} from 'react'

export default class Page2SubComponent extends Component {
  render () {
    return (
      <div>
        <h4>Page2SubComponent</h4>
        with id: <strong>{this.props.params.id}</strong>
      </div>
    )
  }
}

Page2SubComponent.propTypes = {
  params: PropTypes.shape({
    id: PropTypes.string
  })
}

Page2SubComponent.defaultProps = {

}
