#!/usr/bin/env python


def read_file(path):
	txt = None
	try:
		with open(path, 'r') as handle:
			txt = handle.read()
	except IOError, err:
		print "Error: %s" % err

	return txt


barcode_tmpl = read_file('./barcode_template')

code_arr = [] 

for i in range(1,7):
	code_arr.append('BI00%02dL4' % i)
	code_arr.append('BI00%02dL4' % i)

print (barcode_tmpl % tuple(code_arr))
