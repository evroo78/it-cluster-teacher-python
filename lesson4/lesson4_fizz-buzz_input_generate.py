# створюємо вихідний файл для fizzbuzz
import random
import sys

if len(sys.argv)-1: # назва файлу
	filename = sys.argv[1]
else:
	filename = "in.txt"
if len(sys.argv)-2 > 0: # кількість завдань
	n = int(sys.argv[2])
else:
	n = 20

f = open(filename, 'w')
for i in range(n):
	number = random.randrange(10,30)
	buzz = random.randrange(number//2,number-1)
	fizz = random.randrange(2,buzz-1)
	f.write(f'{fizz} {buzz} {number}\n')