import React, { Component } from 'react';
import ExpandedFlightRow from './ExpandedFlightRow.js'
import SmoothCollapse from 'react-smooth-collapse'
import FlightRowIssueSymbols from './FlightRowIssueSymbols.js'

class FlightRow extends Component {
  constructor() {
   super();
   this.state = {
     open: false
   };
  }

  render() {
    return (
      <div className="row-container flight-info-row">
        <div
          className={'columns ' + this.props.status}
          onClick={() => {
            this.setState({
              ...this.state,
              open: !this.state.open
            }
            )
          }}
        >
          <div className="status">
            <div className="column">{this.props.info.PLAN_CARRIER_CODE + this.props.info.PLAN_FLIGHT_NUMBER}</div>
            <div className="column">{this.props.info.PLAN_DEPARTURE_STATION}</div>
            <div className="column">{this.props.info.PLAN_ARRIVAL_STATION}</div>
            <div className="column">{this.props.info.PLAN_DEPARTURE_DATETIME_LOCAL}</div>
            <div className="column">{this.props.info.PLAN_ARRIVAL_DATETIME_LOCAL}</div>
            <div className="column" style={{'flexGrow': 10}}>
              Magic data that still needs to be gathered
{/*
  <FlightRowIssueSymbols issues={this.props.info.issues}/>
  */
}
            </div>
          </div>
          <div className="detail">
            <SmoothCollapse
              expanded={this.state.open}
              heightTransition=".2s"
            >
              <ExpandedFlightRow flightIndex={this.props.flightIndex} open={this.state.open} status={this.props.status} />
            </SmoothCollapse>
          </div>
        </div>
      </div>
    );
  }
}

export default FlightRow;
