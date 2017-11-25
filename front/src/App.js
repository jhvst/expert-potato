import React, { Component } from 'react';
import logo from './finnair.svg';
import './App.css';
import FlightRow from './FlightRow.js'

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="container">
          <header className="App-header">
            <img src={logo} className="App-logo" alt="logo" />
            <h1 className="title">Expert potato</h1>
          </header>
          <hr />
          <table className="table">
            <thead>
              <tr>
                <th>Flight#</th>
                <th>From</th>
                <th>To</th>
                <th>Weather</th>
                <th>Airspace</th>
                <th>Strikes</th>
                <th>Enviromental</th>
                <th>Airport closure</th>
                <th>National</th>
                <th>Large events</th>
                <th>Political conflicts</th>
                <th>Military operations</th>
              </tr>
            </thead>
            <tbody>
              <FlightRow />
              <FlightRow />
              <FlightRow />
            </tbody>
          </table>
        </div>
      </div>
    );
  }
}

export default App;
