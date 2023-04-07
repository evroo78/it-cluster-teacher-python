n = int(input())

print (1, end=" ")
for i in range(2,n//2+1):
	if not n%i:
		print(i, end=" ")
print(n)