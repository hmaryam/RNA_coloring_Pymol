'''
In pymol terminal:
run test2QBG.py
color 2QBG
'''
import sys
import cmd
import csv

reader = csv.reader(open("2QBG.csv", 'rb'), delimiter=",")

def split_range(nt_range):
	'''
	Imput :' 1 -- 9 / 35 -- 38 '
	Output : [('1','9'), ('35','38')]
	'''
	nt_range = nt_range.strip()
	if nt_range=="Not Present":
		return ''
	if len(nt_range)==0:
		return ''
	if '0' <= nt_range[0] <='9':
		split1= nt_range.split('/')
		split2= '\n'.join(split1)
		nt_number = ''.join(split2.split('--'))
		a=  nt_number.split()
		it = iter(a)
		d= zip(it, it)
		return d
	else:
		return ''

def convert_color_RGB(colorr):
	'''
	RGB colores are not defined in pymol.
	convert_color_RBG function defines RGB colors
	Input : '#3300FF'
	Output : "RGB_blue" ( which we have defined to be [51 , 0 , 255] )
	'''
	cmd.set_color( 'RGB_blue' , [51 , 0 , 255] )
	cmd.set_color( 'RGB_green' , [51 , 153 , 51] )
	cmd.set_color( 'RGB_Lblue' , [51 , 153 , 255] )
	cmd.set_color( 'RGB_grey' , [128 , 128 , 128] )
	cmd.set_color( 'RGB_brown' , [139 , 69 , 19] )
	cmd.set_color( 'RGB_purple' , [153 , 30 , 255] )
	cmd.set_color( 'RGB_gold' , [205 , 173 , 0] )
	cmd.set_color( 'RGB_red' , [255 , 0 , 51] )
	cmd.set_color( 'RGB_orange' , [255 , 102 , 0] )

	if colorr == "#3300FF":
		return "RGB_blue"
	elif colorr == "#339933":
		return "RGB_green"
	elif colorr == "#3399FF":
		return "RGB_Lblue"
	elif colorr == "#808080":
		return "RGB_grey"
	elif colorr == "#8B4513":
		return "RGB_brown"
	elif colorr == "#991EFF":
		return "RGB_purple"
	elif colorr == "#CDAD00":
		return "RGB_gold"
	elif colorr == "#FF0033":
		return "RGB_red"
	elif colorr == "#FF6600":
		return 'RGB_orange'
	else:
		return 'white'

# ntd = [('1', '9'), ('2886', '2897')]
# ntdList = (data) = [('31_32', 'blue'), ('57_70', 'Purple'),....]
def nt_ranges(reader):
	'''
	This function gives a list of tuples with the range of nucletides and their corresponding defined color
	ntd = [('1', '9'), ('2886', '2897'), ...]
	Output : ntdList = (data) = [('31_32', 'blue'), ('57_70', 'Purple'),....]
	'''
	ntdList=[]
	for i, line in enumerate(reader):
		ntd = split_range(line[1])
		ntd_color = convert_color_RGB(line[0])
		chain = line[2]
		if len(ntd)==1: # just one range [('1', '9')]
			ntdList += [((ntd[0][0])+'-'+(ntd[0][1]), ntd_color, line[2])]
		if len(ntd)==2:
				ntdList += [((ntd[0][0])+'-'+(ntd[0][1]), ntd_color, line[2])]
				ntdList += [((ntd[1][0])+'-'+(ntd[1][1]), ntd_color, line[2])]
	#print len(ntdList)
	return ntdList


def color_structure(pdb_file):
	'''
	this function colors each nucleotide in pymol
	>>>print (data[1][0])
	2886_2897	

	2QBG must match the name of pdb file which is open 
	data[i][1] = color
	data[i][0] = range of nucleotide
	data[i][2] = chain

	'''
	data = nt_ranges(reader)
	for i in range(0,len(data)):
		if (data[i][2]) != '':
			cmd.color(data[i][1], "%s and resi %s in chain %s" % ( pdb_file, data[i][0], data[i][2]))
		elif(data[i][2]) == '':
			cmd.color(data[i][1], "%s and resi %s " % ( pdb_file, data[i][0]))
cmd.extend('color', color_structure)