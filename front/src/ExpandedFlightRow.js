import React, { Component } from 'react';
import mockupExpandedData from './mockupexpandeddata.js'

class ExpandedFlightRow extends Component {
  render() {

    return (
      <span>
        <div className={this.props.status} style={{'display': 'flex', 'flexDirection': 'row'}}
          onClick={() => {
          }}
        >
          <div className='column'>
            <div className="box">
              <p className='subtitle'>Flight <b>{ mockupExpandedData[0].PLAN_CARRIER_CODE + mockupExpandedData[0].PLAN_FLIGHT_NUMBER }</b></p>
              <ul>
                <li>Seq number: {mockupExpandedData[0].PLAN_FLIGHT_SEQ_NUMBER}</li>
                <li>Local departure date: {mockupExpandedData[0].PLAN_DEPARTURE_DATETIME_LOCAL}</li>
                <li>Local arrival date: {mockupExpandedData[0].PLAN_ARRIVAL_DATETIME_LOCAL}</li>
                <li>Departure airport: {mockupExpandedData[0].PLAN_DEPARTURE_STATION}</li>
                <li>Arrival airport: {mockupExpandedData[0].PLAN_ARRIVAL_STATION}</li>
                <li>Aircraft owner: {mockupExpandedData[0].PLAN_AC_OWNER}</li>
                <li>Aircraft service type: {mockupExpandedData[0].PLAN_SERVICE_TYPE}</li>
                <li>Aircraft type: {mockupExpandedData[0].PLAN_AC_TYPE}</li>
              </ul>
            </div>
          </div>
          <div className='column'>
            <div className='box'>
              <p className='subtitle'>Risks</p>
              <div className="media-content">
                Some risk information about relevant cause. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
              </div>
            </div>
          </div>
          <div className='column'>
            <div className='box'>
              <p className='subtitle'>Stats</p>
            </div>
          </div>
        </div>
      </span>
    )
  }
}

export default ExpandedFlightRow;
