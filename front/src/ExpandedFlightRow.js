import React, { Component } from 'react';

class ExpandedFlightRow extends Component {
  render() {
    if (this.props.open) {
      return (
        <div
          onClick={() => {
            console.log('yes')
          }}
        >
          <h1 className='title'>More magic info</h1>
        </div>
      )
    } else {
      return ''
    }
  }
}

export default ExpandedFlightRow;
