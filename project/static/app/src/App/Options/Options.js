import React, {Component} from 'react'
import {observer} from 'mobx-react'

@observer
export default class Options extends Component {
  render () {
    const options = this.props.options.map((option) => {
      return (
        <tr key={option.branch}>
          <td>{option.branch}</td>
          <td>{option.description}</td>
        </tr>
      )
    })

    return (
      <table className="table">
        <thead>
          <tr><th>branch</th><th>feature</th></tr>
        </thead>
        <tbody>
          {options}
        </tbody>
      </table>
    )
  }
}
