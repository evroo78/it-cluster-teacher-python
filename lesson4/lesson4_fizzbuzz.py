# Написати fizzbuzz для 20 комплектів по три числа, які записані в файл. Читайте із файлу перший рядок з трьома числами, беріть із нього числа, рахуйте для них fizzbuzz, виводите, продовжуйте з наступним рядком і так до кінця файла.

import sys
if len(sys.argv)-1: # input file
	filename_in = sys.argv[1]
else:
	filename_in = "in.txt"

if len(sys.argv)-1: #output file
	filename_out = sys.argv[1]
else:
	filename_out = "out.txt"

f_in = open(filename_in, 'r')
f_out = open(filename_out, 'w')

def fizzbuzz(fizz, buzz, number):
	answer = ""
	for i in range(1,number+1):
		# print(i)
		if not i % fizz:
			answer+="F"
		if not i % buzz:
			answer+="B"
		if i % buzz and i % fizz:
			answer+=str(i)+" "
		else:
			answer+=" "
	return(answer)


for line in f_in:
	fizz,buzz,number = map(int,line.split())
	# print(fizz, buzz, number)
	result = fizzbuzz(fizz, buzz, number)
	print(f"{line[:-1]}: {result}")
	f_out.write(result+"\n")

f_in.close()
f_out.close()