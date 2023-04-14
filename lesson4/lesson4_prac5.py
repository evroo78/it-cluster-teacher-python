#Банкомат видає суму дрібними, але не більше 10 штук кожної дрібної купюри

nominals = [10, 20, 50, 100, 200, 500, 1000]
counts = [0]*7

money = int(input())
print(f"{money} UAH ATM dispenses:")

if money%10 > 0:
	print("It's no posible!")
else:
	inom = 0
	while money > 0:
		if money > nominals[inom] *10:
			counts[inom] = 10
			money -= nominals[inom] *10
		else:
			while money % nominals[inom]:
				counts[inom-1] -= 1
				money += nominals[inom-1]
			counts[inom] = money // nominals[inom]
			money %= nominals[inom]
		inom+=1

	# Print of result
	n = len(nominals)
	for i in range(n):
		if counts[i]:
			print(f"{counts[i]} banknotes of {nominals[i]} UAH")