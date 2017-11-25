package main

import (
	"bufio"
	"bytes"
	"encoding/csv"
	"encoding/json"
	"encoding/xml"
	"io/ioutil"
	"net/http"
)

type Symbol struct {
	Status string `xml:"name,attr"`
}

type Timestamp struct {
	Symbol Symbol `xml:"symbol"`
}

type Tabular struct {
	Timestamp []Timestamp `xml:"time"`
}

type Forecast struct {
	Tabular Tabular `xml:"tabular"`
}

type Location struct {
	Name string `xml:"name"`
}

type Result struct {
	XMLName  xml.Name `xml:"weatherdata"`
	Location Location `xml:"location"`
	Forecast Forecast `xml:"forecast"`
}

type AirportStatus struct {
	Abbr     string
	City     string
	Statuses []string
}

var airportsToSearch = []string{}

func contains(a string) bool {
	for _, airport := range airportsToSearch {
		if a == airport {
			return true
		}
	}
	return false
}

var Statuses []AirportStatus

func main() {

	codes, _ := ioutil.ReadFile("codes.txt")
	scanner := bufio.NewScanner(bytes.NewReader(codes))
	for scanner.Scan() {
		airportsToSearch = append(airportsToSearch, scanner.Text())
	}

	airports, _ := ioutil.ReadFile("airports.csv")
	r := csv.NewReader(bytes.NewReader(airports))
	records, _ := r.ReadAll()

	for _, r := range records {
		abbrv := r[4]
		if contains(abbrv) {
			airportName := r[2]
			Statuses = append(Statuses, AirportStatus{
				Abbr: abbrv,
				City: airportName,
			})
		}
	}

	weather, _ := ioutil.ReadFile("yrno.csv")
	wr := csv.NewReader(bytes.NewReader(weather))
	wrecords, _ := wr.ReadAll()

	for i, statuses := range Statuses {
		Statuses[i].Statuses = getWeather(statuses.City, wrecords)
	}

	output, _ := json.Marshal(Statuses)
	ioutil.WriteFile("airports.json", output, 0666)
}

func getWeather(city string, wrecords [][]string) []string {
	s := make([]string, 0)
	for _, location := range wrecords {
		if location[3] == city {

			resp, _ := http.Get(location[15])
			data, _ := ioutil.ReadAll(resp.Body)

			var result Result
			xml.Unmarshal(data, &result)

			for _, status := range result.Forecast.Tabular.Timestamp {
				s = append(s, status.Symbol.Status)
			}
		}
	}
	return s
}
