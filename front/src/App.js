import React, { Component } from 'react';
import logo from './finnair.svg';
import './App.css';
import FlightRows from './FlightRows.js'
import mockupRows from './mockupdata'
import flightSchedule from './flightSchedule.js'
import Fuse from 'fuse.js'

// fuzzy search option
const options = {
  shouldSort: true,
  threshold: 0.6,
  location: 0,
  distance: 100,
  maxPatternLength: 32,
  minMatchCharLength: 1,
  keys: [
    "PLAN_DEPARTURE_STATION",
    "PLAN_ARRIVAL_STATION",
    "PLAN_FLIGHT_NUMBER"
]
};
const fuse = new Fuse(flightSchedule, options); // "list" is the item array


class App extends Component {
  constructor() {
   super();
   this.state = {
     searchText: ''
   };
  }
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
        </header>
        <div className="container">
          <div className="leading">
            <h3>What is the chance an upcoming flight will have delays?</h3>
            <ul>
              <li><span style={{'color': '#2ecc71'}}>green</span> means the flight <b>is on time</b> -- no threaths for a possible delay are identified</li>
              <li><span style={{'color': '#f1c40f'}}>yellow</span> means the flight <b>may be delayed</b> -- the software has picked the first signs of delay factors</li>
              <li><span style={{'color': '#e74c3c'}}>red</span> means the flight <b>is likely to be delayed</b> -- the software has picked and verified multiple signs for delay factors</li>
            </ul>
          </div>
          <div className="field">
            <div className="control">
              <input
                className="input"
                type="text"
                placeholder="Filter data"
                onChange={(i) => {
                  this.setState({
                    ...this.state,
                    searchText: i.target.value
                  })
                }}
              />
            </div>
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
              <FlightRows
                data={
                  this.state.searchText.length===0
                  ? flightSchedule
                  : fuse.search(this.state.searchText)
                } />
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
