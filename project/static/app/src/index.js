import Routes from './Routes'
import React from 'react'
import ReactDOM from 'react-dom'
import Backendless from 'backendless'

var APPLICATION_ID = 'B73655FB-1EF0-1428-FFEB-5B02147B8200'
var SECRET_KEY = 'AF4167F1-7E8B-AC3B-FFBE-7EA82175F000'
var VERSION = 'v1'

Backendless.initApp(APPLICATION_ID, SECRET_KEY, VERSION)

ReactDOM.render(
	<Routes/>, document.getElementById('app-root')
)
