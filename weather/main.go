package main

import (
	"bufio"
	"bytes"
	"encoding/csv"
	"encoding/json"
	"encoding/xml"
	"io/ioutil"
	"net/http"
	"strings"
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
	Abbr  string
	City  string
	Mode  string
	Risks []string
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
		Statuses[i].Risks, Statuses[i].Mode = getWeather(statuses.City, wrecords)
	}

	output, _ := json.Marshal(Statuses)
	ioutil.WriteFile("airports.json", output, 0666)
}

func getWeather(city string, wrecords [][]string) ([]string, string) {
	risks := make([]string, 0)
	mode := "Sunny"
	for _, location := range wrecords {
		if location[3] == city {

			resp, _ := http.Get(location[15])
			data, _ := ioutil.ReadAll(resp.Body)

			var result Result
			xml.Unmarshal(data, &result)

			var statusMap = make(map[string]int)
			for _, status := range result.Forecast.Tabular.Timestamp {
				if strings.Contains(status.Symbol.Status, "heavy") {
					risks = append(risks, status.Symbol.Status)
				}
				if strings.Contains(status.Symbol.Status, "Heavy") {
					risks = append(risks, status.Symbol.Status)
				}
				if strings.Contains(status.Symbol.Status, "thunder") {
					risks = append(risks, status.Symbol.Status)
				}
				if val, ok := statusMap[status.Symbol.Status]; ok {
					statusMap[status.Symbol.Status] = val + 1
					continue
				}
				statusMap[status.Symbol.Status] = 0
			}

			var high = 0
			for k, v := range statusMap {
				if v > high {
					mode = k
				}
			}

		}
	}

	return risks, mode
}
