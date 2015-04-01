import cmd
import csv
import urllib2

url = 'https://raw.githubusercontent.com/hmaryam/pymol/master/color_p.csv'
response = urllib2.urlopen(url)
reader = csv.reader(response, delimiter=",")


for i, line in enumerate(reader):
	print line
