import React, { Component } from 'react';
import logo from './finnair.svg';
import './App.css';
import FlightRow from './FlightRow.js'
import mockupRows from './mockupdata'


class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
        </header>
        <div className="container">
          <div className="flight-table">
            <div className="detail-wrapper">
              <div className="columns-header">
                <div className="column">Flight#</div>
                <div className="column">From</div>
                <div className="column">To</div>
                <div className="column">Dep</div>
                <div className="column">Arr</div>
                <div className="column" style={{'flexGrow': 10}}>Issues</div>
              </div>
          {mockupRows.map((item) => {
            return (
              <FlightRow key={item.info.flight} status={item.status} info={item.info} />
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
