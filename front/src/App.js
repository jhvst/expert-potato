import React, { Component } from 'react';
import logo from './illaksikotiin.png';
import './App.css';
import FlightRows from './FlightRows.js'
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
            <p>We are scraping data from Twitter, thousands of news sources and weather data to predict the likelihood of flight delay or cancellation.</p>
          </div>
          <div className="field">
            <div className="control">
              <input
                className="input"
                type="text"
                placeholder="Search with airport code (AMS) or flight number"
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
                <div className="column" style={{'flexGrow': 5}}>Source</div>
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
