def SplitOneRange(range):
	split1= range.split('/')
	split2= ''.join(split1)
	nt_number = ''.join(split2.split('--'))
	a=  nt_number.split()
	it = iter(a)
	d= zip(it, it)
	#print d
	print d
	for A in d:
		print A
SplitOneRange(' 57 -- 70 / 90 -- 100')
