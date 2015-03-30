import cmd
import csv

f = open("coloring.csv", "rb")
reader = csv.reader(f, delimiter=",")

'''
' 1--7 / 31 -- 32' => [('3','7'), ('31', '32')]
'''
def split_range(range):

	range = range.strip()
	if range=="Not Present":
		return ''
	if len(range)==0:
		return ''
	if '0' <= range[0] <='9':
		split1= range.split('/')
		split2= '\n'.join(split1)
		nt_number = ''.join(split2.split('--'))
		a=  nt_number.split()
		it = iter(a)
		d= zip(it, it)
		return d
	else:
		return ''

def convert_color(colorr):
	if colorr == "#3300FF":
		return "red"
	elif colorr == "#339933":
		return "blue"
	elif colorr == "#3399FF":
		return "Genumeratereen"
	elif colorr == "#339933":
		return "Black"
	elif colorr == "#808080":
		return "Yellow"
	elif colorr == "#8B4513":
		return "Grey"
	elif colorr == "#991EFF":
		return "Orange"
	elif colorr == "#CDAD00":
		return "White"
	elif colorr == "#FF0033":
		return "Purple"
	elif colorr == "#FF6600":
		return 'Pink'
	else:
		return ''



def ntd(color, ranges):

#it will give a list of tuples. [(ntd1 number, ntd1 color), (ntd2 number, ntd2 color),..]

	ntdList=[]
    # like : '1--9' => [('1','9')]
	if len(ranges)==1:
		for i in range(int(ranges[0][0]),int(ranges[0][1])+1):
			ntdList+= [(i, color)]
	# like : '1--9 / 31 -- 32 ' => [('1','9'), ('31', '32')]
	if len(ranges)==2:
		for i in range(int(ranges[0][0]),int(ranges[0][1])+1):
			ntdList+= [(i, color)]
		for i in range(int(ranges[1][0]),int(ranges[1][1])+1):
			ntdList+= [(i, color)]
	return ntdList



def ntd2(reader):
	'''
	line is a list : ['color', ' nucleotide ranges' ]
	example : ["#3300FF", '1--9 / 31 -- 32 ' ]
	'''
	ntdList=[]

	for i, line in enumerate(reader):
		ranges = split_range(line[1])
		ccolor = convert_color(line[0])
		if len(ranges)==1:
			for i in range(int(ranges[0][0]),int(ranges[0][1])+1):
				ntdList+= [(i, ccolor)]

		if len(ranges)==2:
			for i in range(int(ranges[0][0]),int(ranges[0][1])+1):
				ntdList+= [(i, ccolor)]
			for i in range(int(ranges[1][0]),int(ranges[1][1])+1):
				ntdList+= [(i, ccolor)]
	return ntdList

def cmd_color(data):
	for i in data:
		cmd.color(convert_color(data[i][1]), "4QS1 and resi " +str(data[i][0]))
	

x = ntd2(reader)
cmd_color(x)
   



