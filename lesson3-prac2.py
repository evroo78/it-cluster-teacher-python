n = int(input())

if n%2 and (not n%3) and (not n%5) and n%10:
	print(f'{n} satisfies the conditions')
else:
	print(f'{n} does not satisfy the conditions')