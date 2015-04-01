import cmd
import csv

l=[]
with open("coloring.csv", "rb") as f:
    reader = csv.reader(f, delimiter=",")
    for i, line in enumerate(reader):
    #	l.append(line)
		print line 


def SplitOneRange(range):
	split1= range.split('/')
	split2= '\n'.join(split1)
	nt_number = ''.join(split2.split('--'))
	a=  nt_number.split()
	it = iter(a)
	d= zip(it, it)
	print d
# ('31', '32'), ('473', '474')]
#def color_convert(color):
#	'#8B4513'=,,,,
#for i in x"
cmd.color("purpleblue", "4QS1 and resi" +'9')