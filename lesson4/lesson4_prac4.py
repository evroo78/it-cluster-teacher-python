#Банкомат видає суму максимально можливими купюрами

nominals = [10, 20, 50, 100, 200, 500, 1000]
counts = [0]*7

money = int(input())
print(f"{money} UAH ATM dispenses:")

if money%10 > 0:
	print("It's no posible!")
else:
	inom = 1
	while money > 0:
		counts[-inom] = money // nominals[-inom]
		money %= nominals[-inom]
		inom +=1

	# Print of result
	n = len(nominals)
	for i in range(n):
		if counts[i]:
			print(f"{counts[i]} banknotes of {nominals[i]} UAH")