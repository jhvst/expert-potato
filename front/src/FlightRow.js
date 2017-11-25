import React, { Component } from 'react';
import ExpandedFlightRow from './ExpandedFlightRow.js'

class FlightRow extends Component {
  render() {
    return (
      <span className="row-container">
        <div
          className={'columns ' + this.props.status}
          onClick={() => {
            console.log('yes')
          }}
        >
          <div className="column">AYY135</div>
          <div className="column">HEL</div>
          <div className="column">SFO</div>
          <div className="column"><i className="fa fa-cloud" aria-hidden="true"></i></div>
          <div className="column"><i className="fa fa-globe" aria-hidden="true"></i></div>
          <div className="column"><i className="fa fa-users" aria-hidden="true"></i></div>
          <div className="column"><i className="fa fa-tree" aria-hidden="true"></i></div>
          <div className="column"><i className="fa fa-plane" aria-hidden="true"></i></div>
          <div className="column"><i className="fa fa-flag" aria-hidden="true"></i></div>
          <div className="column"><i className="fa fa-futbol-o" aria-hidden="true"></i></div>
          <div className="column"><i className="fa fa-briefcase" aria-hidden="true"></i></div>
          <div className="column"><i className="fa fa-rocket" aria-hidden="true"></i></div>
        </div>
        <ExpandedFlightRow open={this.props.open} />
      </span>
    );
  }
}

export default FlightRow;
