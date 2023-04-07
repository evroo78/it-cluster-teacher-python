# Ввести число, вивести його розряди та їх множники.
# Не виводить 0 та якщо 1 виводить тільки 10 у певнй ступіні

n = int(input())

def output(num,power,s="+"):
	if num:
		if num>1:
			print (f'{num}',end="")
		if num>1 and power:
			print("*",end="")
		if power:
			print (f'10^{power}',end="")
		print(s,end="")

power = 0
while n>=10:
	temp = n%10
	n = n//10
	output(temp, power)
	power+=1

output(n, power,"\n")