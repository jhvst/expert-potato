import csv
import sys  


def parse_destinations(filename):
	names = []
	
	with open(filename, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='"')
		firstRead = False
		for row in reader:
			if firstRead:
				names.append(row[16])
				names.append(row[17])
			firstRead = True
				
			#print(row[16], row[17])
		
	names = set(names)
	return names

		
def parse_airports(filename):
	airports = {}
	
	with open(filename, 'r', encoding="utf-8") as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='"')
		firstRead = False
		for row in reader:
			if firstRead:
				airports[row[13]] = row[3]
				#names.append(row[17])
			firstRead = True
	
	return airports
	

dests = parse_destinations('Flight_Schedule.csv')
airports = parse_airports('airports.csv')

with open('finnair_airports.csv', 'w', encoding='utf-8', newline='') as csvfile:
	writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
	for c in dests:
		writer.writerow((c, airports[c]))
	

for c in dests:
	print(c, airports[c])

