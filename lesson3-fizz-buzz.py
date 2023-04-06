fizz = int(input())
buzz = int(input())
number = int(input())


for i in range(1,number+1):
	answer = ""
	if not i % fizz:
		answer+="F"
	if not i % buzz:
		answer+="B"
	if answer:
		print(answer, end=" ")
	else:
		print(i, end=" ")
