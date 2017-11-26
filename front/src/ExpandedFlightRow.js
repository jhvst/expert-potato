import React, { Component } from 'react';
import flightSchedule from './flightSchedule.js'
import flightWeather from './flightWeather.js'
import _ from 'underscore';
var flightWeatherMap = _.indexBy(flightWeather, 'Abbr');

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
              <p className='subtitle'>Flight <b>{ flightSchedule[this.props.flightIndex].PLAN_CARRIER_CODE + flightSchedule[this.props.flightIndex].PLAN_FLIGHT_NUMBER }</b></p>
              <div className='columns' style={{'flexDirection':'row', 'boxShadow':'none'}}>
                <div className='column' style={{'fontWeight':'bold'}}>Seq number:</div>
                <div className='column'> {flightSchedule[this.props.flightIndex].PLAN_FLIGHT_SEQ_NUMBER}</div>
              </div>
              <div className='columns' style={{'flexDirection':'row', 'boxShadow':'none'}}>
                <div className='column' style={{'fontWeight':'bold'}}>Departure date:</div>
                <div className='column'> {flightSchedule[this.props.flightIndex].PLAN_DEPARTURE_DATETIME_UTC}</div>
              </div>
              <div className='columns' style={{'flexDirection':'row', 'boxShadow':'none'}}>
                <div className='column' style={{'fontWeight':'bold'}}>Arrival date:</div>
                <div className='column'> {flightSchedule[this.props.flightIndex].PLAN_ARRIVAL_DATETIME_UTC}</div>
              </div>
              <div className='columns' style={{'flexDirection':'row', 'boxShadow':'none'}}>
                <div className='column' style={{'fontWeight':'bold'}}>Departure airport:</div>
                <div className='column'> {flightSchedule[this.props.flightIndex].PLAN_DEPARTURE_STATION} / {flightSchedule[this.props.flightIndex].departureAirport}</div>
              </div>
              <div className='columns' style={{'flexDirection':'row', 'boxShadow':'none'}}>
                <div className='column' style={{'fontWeight':'bold'}}>Arrival airport:</div>
                <div className='column'> {flightSchedule[this.props.flightIndex].PLAN_ARRIVAL_STATION} / {flightSchedule[this.props.flightIndex].arrivalAirport}</div>
              </div>
              <div className='columns' style={{'flexDirection':'row', 'boxShadow':'none'}}>
                <div className='column' style={{'fontWeight':'bold'}}>Aircraft owner:</div>
                <div className='column'> {flightSchedule[this.props.flightIndex].PLAN_AC_OWNER}</div>
              </div>
              <div className='columns' style={{'flexDirection':'row', 'boxShadow':'none'}}>
                <div className='column' style={{'fontWeight':'bold'}}>Aircraft service type:</div>
                <div className='column'> {flightSchedule[this.props.flightIndex].PLAN_SERVICE_TYPE}</div>
              </div>
              <div className='columns' style={{'flexDirection':'row', 'boxShadow':'none'}}>
                <div className='column' style={{'fontWeight':'bold'}}>Aircraft type:</div>
                <div className='column'> {flightSchedule[this.props.flightIndex].PLAN_AC_TYPE}</div>
              </div>
            </div>
          </div>
          <div className='column'>
            <div className='box'>
              <p className='subtitle'>Risks</p>
              <div className="media-content">
                {
                  flightSchedule[this.props.flightIndex].threat.map((singleRisk, i) => {
                    console.log(singleRisk)
                    return singleRisk.source === 'twitter'
                    ? <div key={i} className="box"><div className="subtitle">Tweet:</div> {singleRisk.twitter_message} </div>
                    : <div key={i} className="box"><div className="subtitle">News article:</div> {singleRisk.article_title} </div>
                  })
                }
              </div>
            </div>
          </div>
          <div className='column'>
            <div className='box'>
              <p className='subtitle'>Weather</p>
              <div className="media-content">
                <div className="box">
                  Weather in {flightSchedule[this.props.flightIndex].PLAN_DEPARTURE_STATION}: { flightWeatherMap[flightSchedule[this.props.flightIndex].PLAN_DEPARTURE_STATION].Mode }
                </div>
                { flightWeatherMap[flightSchedule[this.props.flightIndex].PLAN_DEPARTURE_STATION].Risks.length > 0
                  ? <div className="box"><i class="fa fa-exclamation-triangle" aria-hidden="true"></i>&nbsp;
  Weather risks in the place of departure: <br /> { flightWeatherMap[flightSchedule[this.props.flightIndex].PLAN_DEPARTURE_STATION].Risks[0] } </div>
                  : ''
                }

              </div>
              <br />
              <div className="media-content">
                <div className="box">
                  Weather in {flightSchedule[this.props.flightIndex].PLAN_ARRIVAL_STATION}: { flightWeatherMap[flightSchedule[this.props.flightIndex].PLAN_ARRIVAL_STATION].Mode }
                </div>
                { flightWeatherMap[flightSchedule[this.props.flightIndex].PLAN_ARRIVAL_STATION].Risks.length > 0
                  ? <div className="box"><i class="fa fa-exclamation-triangle" aria-hidden="true"></i>&nbsp;
  Weather risks in the place of arrival: <br /> { flightWeatherMap[flightSchedule[this.props.flightIndex].PLAN_ARRIVAL_STATION].Risks[0] } </div>
                  : ''
                }
              </div>
            </div>
          </div>
        </div>
      </span>
    )
  }
}

export default ExpandedFlightRow;
