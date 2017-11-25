import React, { Component } from 'react';
import ExpandedFlightRow from './ExpandedFlightRow.js'
import SmoothCollapse from 'react-smooth-collapse'

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
            console.log('here')
            this.setState({
              ...this.state,
              open: !this.state.open
            }
            )
          }}
        >
          <div className="column">AYY135</div>
          <div className="column">HEL</div>
          <div className="column">SFO</div>
          <div className="column">18:00</div>
          <div className="column">22:00</div>          
          <div className="column">
            <i className="fa fa-cloud" aria-hidden="true"></i>
            <i className="fa fa-globe" aria-hidden="true"></i>
            <i className="fa fa-users" aria-hidden="true"></i>
            <i className="fa fa-tree" aria-hidden="true"></i>
            <i className="fa fa-plane" aria-hidden="true"></i>
            <i className="fa fa-flag" aria-hidden="true"></i>
            <i className="fa fa-futbol-o" aria-hidden="true"></i>
            <i className="fa fa-briefcase" aria-hidden="true"></i>
            <i className="fa fa-rocket" aria-hidden="true"></i>
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
