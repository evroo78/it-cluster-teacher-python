# Кожен пише суму списку за допомогою for та while

import random
n = 10
main_list = [random.randrange(50) for i in range(10)]

# Path 1 "FOR"
summa = 0
for item in main_list:
	summa += item
print (summa)

#Path 2 "WHILE"
item, summa = 0, 0
while item<n:
	summa += main_list[item]
	item += 1
print(summa)
