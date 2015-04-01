import cmd
import csv
import urllib2

url = 'https://raw.githubusercontent.com/hmaryam/pymol/master/4QS1_coloring_info.csv' 
response = urllib2.urlopen(url)
reader = csv.reader(response, delimiter=",")

	
for i, x in enumerate(reader):
		print x[2]


