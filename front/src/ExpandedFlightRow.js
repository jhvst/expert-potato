import React, { Component } from 'react';

class ExpandedFlightRow extends Component {
  render() {
    return (
      <div class={this.props.status} style={{'display': 'flex', 'flexDirection': 'row'}}
        onClick={() => {
          console.log('yes')
        }}
      >
        <div className='column'>
          <div className="box">
            <p className='subtitle'>Flight <b>AYY135</b></p>
            <ul>
              <li>PLAN_CARRIER_CODE</li>
              <li>PLAN_FLIGHT_NUMBER</li>
              <li>PLAN_FLIGHT_NUMBER_CHAR4</li>
              <li>PLAN_FLIGHT_SEQ_NUMBER</li>
              <li>PLAN_DEPARTURE_DATETIME_LOCAL</li>
              <li>PLAN_DEPARTURE_DATE_LOCAL</li>
              <li>PLAN_DEPARTURE_TIME_LOCAL</li>
              <li>PLAN_DEPARTURE_DATETIME_UTC</li>
              <li>PLAN_DEPARTURE_DATE_UTC</li>
              <li>PLAN_DEPARTURE_TIME_UTC</li>
              <li>PLAN_ARRIVAL_DATETIME_LOCAL</li>
              <li>PLAN_ARRIVAL_DATE_LOCAL</li>
              <li>PLAN_ARRIVAL_TIME_LOCAL</li>
              <li>PLAN_ARRIVAL_DATETIME_UTC</li>
              <li>PLAN_ARRIVAL_DATE_UTC</li>
              <li>PLAN_ARRIVAL_TIME_UTC</li>
              <li>PLAN_DEPARTURE_STATION</li>
              <li>PLAN_ARRIVAL_STATION</li>
              <li>PLAN_START_OF_OPERATION</li>
              <li>PLAN_END_OF_OPERATION</li>
              <li>PLAN_DAYS_OF_OPERATION</li>
              <li>PLAN_AC_OWNER</li>
              <li>PLAN_SERVICE_TYPE</li>
              <li>PLAN_AC_TYPE</li>
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
    )
  }
}

export default ExpandedFlightRow;
