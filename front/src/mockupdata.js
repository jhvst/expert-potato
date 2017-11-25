const mockupRows = [
{
  'info': {
    'flight':'AYY135',
    'from':'HEL',
    'to':'SFO',
    'arr':'18:00',
    'dep':'22:00',
    'issues':[
      'weather'
      // 'weather',
      // 'airspace',
      // 'strikes',
      // 'environmental',
      // 'airport closure',
      // 'national',
      // 'large events',
      // 'political conflicts',
      // 'military operations',
      // 'other'
    ]
  },
  'status': 'Warning' //operational, warning, danger
},
{
  'info': {
    'flight':'AYY138',
    'from':'HEL',
    'to':'SFO',
    'arr':'18:00',
    'dep':'22:00',
    'issues':[
      'large events',
      'political conflicts'
    ]
  },
  'status': 'Danger' //operational, warning, danger
},
{
  'info': {
    'flight':'AYY133',
    'from':'HEL',
    'to':'SFO',
    'arr':'18:00',
    'dep':'22:00',
    'issues':[
      'airport closure',
      'other'
    ]
  },
  'status': 'Operational' //operational, warning, danger
}
];

export default mockupRows;
