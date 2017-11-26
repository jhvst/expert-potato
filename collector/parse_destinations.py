import csv
import sys  


def parse_countries(filename):
	countries = {}
	with open(filename, 'r', encoding='utf-8') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='"')
		firstRead = False
		for row in reader:
			if firstRead:
				countries[row[1]] = row[2]
			firstRead = True
	return countries

def parse_codes(filename):
	codes = []
	with open(filename, 'r', encoding='utf-8') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='"')
		firstRead = False
		for row in reader:
			if firstRead:
				codes.append(row[16])
				codes.append(row[17])
			firstRead = True
		
	codes = set(codes)
	return codes

		
def parse_airports(filename, countries):
	airports = {}
	
	with open(filename, 'r', encoding="utf-8") as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='"')
		firstRead = False
		for row in reader:
			if firstRead:
				airports[row[13]] = (row[3], row[10], countries[row[8]])
				#names.append(row[17])
			firstRead = True
	
	return airports
	

dests = parse_codes('Flight_Schedule.csv')
countries = parse_countries('countries.csv')
airports = parse_airports('airports.csv', countries)

with open('finnair_airports.csv', 'w', encoding='utf-8', newline='') as csvfile:
	writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
	for c in dests:
		writer.writerow((c, airports[c][0], airports[c][1], airports[c][2]))
	

for c in dests:
	print(c, airports[c][0], airports[c][1], airports[c][2])

