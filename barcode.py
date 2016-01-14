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

for i in range(17,23):
	code_arr.append('AR10%sL4' % i)
	code_arr.append('AR10%sL4' % i)

print (barcode_tmpl % tuple(code_arr))
