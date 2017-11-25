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
      <span className="row-container">
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
          <div className="column">{this.props.info.flight}</div>
          <div className="column">{this.props.info.from}</div>
          <div className="column">{this.props.info.to}</div>
          <div className="column">{this.props.info.arr}</div>
          <div className="column">{this.props.info.dep}</div>
          <div className="column">
            <FlightRowIssueSymbols issues={this.props.info.issues}/>
          </div>
        </div>
        <SmoothCollapse
          expanded={this.state.open}
          heightTransition=".2s"
        >
          <ExpandedFlightRow open={this.state.open} />
        </SmoothCollapse>
      </span>
    );
  }
}

export default FlightRow;
