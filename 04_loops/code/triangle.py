height = int(input('Enter a height: '))

print(f'\nHere is a triangle of height {height}:')
for i in range(1,height+1):
	for j in range(1,i+1):
		print('*', end="")
	print()
