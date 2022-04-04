import React from "react"
import {
  Chart,
  Geom,
  Axis,
  Tooltip,
} from "bizcharts"

export default class Bar extends React.Component {

  render() {
    // console.log('isVisited: ' + this.props.isVisited)
    let data = this.props.graphData
    const cols = {
      sales: {
        tickInterval: 20
      }
    }
    return (
      <div style={{width: '100%', marginLeft: -30}}>
        <Chart height={338} data={data} scale={cols} forceFit>
          <Axis name="year"/>
          <Axis name="sales"/>
          <Tooltip
            crosshairs={{
              type: "y"
            }}
          />
          <Geom type="interval" position="year*sales"/>
        </Chart>
      </div>
    )
  }
}