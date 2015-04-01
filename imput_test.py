import sys

def get_inputs():
    args = sys.argv[1:]
    if args[0] in ['2GBQ', '2qbg']:
    	return '2QBG'
    else:
    	return 'no'
       

print 'salam %s' %get_inputs()

