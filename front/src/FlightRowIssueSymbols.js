import React, { Component } from 'react';

class FlightRowIssueSymbols extends Component {
  render() {
    return (
      <div>
        {this.props.issues.includes('weather') ? <i className="fa fa-cloud" aria-hidden="true"></i> : ''}
        {this.props.issues.includes('airspace') ? <i className="fa fa-globe" aria-hidden="true"></i> : ''}
        {this.props.issues.includes('environmental') ? <i className="fa fa-users" aria-hidden="true"></i> : ''}
        {this.props.issues.includes('airport closure') ? <i className="fa fa-tree" aria-hidden="true"></i> : ''}
        {this.props.issues.includes('national') ? <i className="fa fa-plane" aria-hidden="true"></i> : ''}
        {this.props.issues.includes('large events') ? <i className="fa fa-flag" aria-hidden="true"></i> : ''}
        {this.props.issues.includes('political conflicts') ? <i className="fa fa-futbol-o" aria-hidden="true"></i> : ''}
        {this.props.issues.includes('military operations') ? <i className="fa fa-briefcase" aria-hidden="true"></i> : ''}
        {this.props.issues.includes('other') ? <i className="fa fa-rocket" aria-hidden="true"></i> : ''}
      </div>
    )
  }
}

export default FlightRowIssueSymbols;
