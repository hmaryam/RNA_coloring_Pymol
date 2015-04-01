import cmd
import csv

f = open("coloring.csv", "rb")
reader = csv.reader(f, delimiter=",")


for i, x in enumerate(reader):
		print x