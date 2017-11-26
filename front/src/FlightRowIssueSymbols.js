import React, { Component } from 'react';

class FlightRowIssueSymbols extends Component {
  render() {
    return (
      <div style={{'fontSize': '2em'}}>
      {
        this.props.issues.map((issue) => {
          return (issue.source == 'newsapi.org') ? <i className="fa fa-newspaper-o" aria-hidden="true"></i> : <i className="fa fa-twitter" aria-hidden="true"></i>
        })
      }
      {/*
        {this.props.issues.includes('weather') ? <span> <i className="fa fa-cloud" aria-hidden="true"></i> Weather</span> : ''}
        {this.props.issues.includes('airspace') ? <span> <i className="fa fa-globe" aria-hidden="true"></i> Airspace</span> : ''}
        {this.props.issues.includes('strike') ? <span> <i className="fa fa-users" aria-hidden="true"></i> Strike</span> : ''}
        {this.props.issues.includes('environmental') ? <span> <i className="fa fa-tree" aria-hidden="true"></i> Environmental</span> : ''}
        {this.props.issues.includes('airport closure') ? <span> <i className="fa fa-plane" aria-hidden="true"></i> Airport closure</span> : ''}
        {this.props.issues.includes('national') ? <span> <i className="fa fa-flag" aria-hidden="true"></i> National</span> : ''}
        {this.props.issues.includes('large events') ? <span> <i className="fa fa-futbol-o" aria-hidden="true"></i> Large events</span> : ''}
        {this.props.issues.includes('political conflicts') ? <span> <i className="fa fa-briefcase" aria-hidden="true"></i> Political conflicts</span> : ''}
        {this.props.issues.includes('military operations') ? <span> <i className="fa fa-rocket" aria-hidden="true"></i> Military operations</span> : ''}
        {this.props.issues.includes('other') ? <span> <i className="fa fa-exclamation" aria-hidden="true"></i> Other</span> : ''}

      */}
      </div>
    )
  }
}

export default FlightRowIssueSymbols;
