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
          <div className="columns columns-header">
                <div className="column">Flight#</div>
                <div className="column">From</div>
                <div className="column">To</div>
                <div className="column">Weather</div>
                <div className="column">Airspace</div>
                <div className="column">Strikes</div>
                <div className="column">Enviromental</div>
                <div className="column">Airport closure</div>
                <div className="column">National</div>
                <div className="column">Large events</div>
                <div className="column">Political conflicts</div>
                <div className="column">Military operations</div>
          </div>
          <FlightRow status='Operational' />
          <FlightRow status='Warning' />
          <FlightRow status='Danger' />
        </div>
      </div>
    );
  }
}

export default App;
