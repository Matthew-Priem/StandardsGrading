num1 = int(input('Enter an integer: '))
num2 = int(input('Enter another integer: '))

print('\nThe multiplication table is:')
for i in range(1,num1+1):
	for j in range(1,num2+1):
		print(f'{i * j:>2}', end="  ")
	print()
