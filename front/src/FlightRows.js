import React, { Component } from 'react';
import FlightRow from './FlightRow.js'

class FlightRows extends Component {
  render() {
    return (
      this.props.data.map((item, i) => {
        return (
          <FlightRow key={item.id} flightIndex={i} status="Operational" info={item} />

        )
      })
    )
  }
}

export default FlightRows;
