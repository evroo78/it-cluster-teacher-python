# Написати програму, яка виводить саму себе задом наперед

import sys
list_of_file = []
filename = sys.argv[0]
f = open(filename, 'r')

for line in f:
	list_of_file.append(line)

for i in reversed(list_of_file):
	print(i,end="")

f.close()
