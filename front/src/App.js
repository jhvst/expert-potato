import React, { Component } from 'react';
import logo from './finnair.svg';
import './App.css';
import FlightRow from './FlightRow.js'
import mockupRows from './mockupdata'
import flightSchedule from './flightSchedule.js'


class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
        </header>
        <div className="container">
          <div className="leading">
            <h3>What's the chance an upcoming flight will have delays?</h3>
            <ul>
              <li><span style={{'color': '#2ecc71'}}>green</span> means the flight <b>is on time</b> -- no threaths for a possible delay are identified</li>
              <li><span style={{'color': '#f1c40f'}}>yellow</span> means the flight <b>may be delayed</b> -- the software has picked the first signs of delay factors</li>
              <li><span style={{'color': '#e74c3c'}}>red</span> means the flight <b>is likely to be delayed</b> -- the software has picked and verified multiple signs for delay factors</li>
            </ul>
          </div>
          <div className="flight-table">
            <div className="detail-wrapper">
              <div className="columns-header">
                <div className="column">Flight#</div>
                <div className="column">From</div>
                <div className="column">To</div>
                <div className="column">Dep</div>
                <div className="column">Arr</div>
                <div className="column" style={{'flexGrow': 10}}>Issues</div>
                <div className="column">&nbsp;</div>
              </div>
          {flightSchedule.map((item, i) => {
            return (
              <FlightRow key={i} flightIndex={i} status="Operational" info={item} />
            )
          })}
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
