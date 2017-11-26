const csvFilePath='./flight_schedule_mar15_30.csv'
const csv=require('csvtojson')
const fs = require('fs')

const airports='./airports.js'


let funkyJsonArr = []

csv()
.fromFile(csvFilePath)
.on('json',(jsonObj)=>{
  console.log(jsonObj)
  let temp = JSON.stringify(jsonObj)
  let departureCode = temp.PLAN_DEPARTURE_STATION
  console.log(departureCode + ' dep')
  let arrivalCode = temp.PLAN_ARRIVAL_STATION
  temp.departureCity = airports.departureCode.city
  temp.arrivalCity = airports.arrivalCode.city
  temp.arrivalAirport = airports.arrivalCode.airport
  temp.departureAirport = airports.departureCode.airport
  funkyJsonArr.push(temp)
})
.on('done',(error)=>{
  fs.writeFile('./flightdata25_30.json', funkyJsonArr, (err) => {
    if (err){
      return console.log(err)
    }
  })

  console.log('end')
})


