def find_factors(num):
	factors = []
	
	for i in range(1, num):
		if num % i != 0:
			factors.add(i)

	return factors

# Test the function with a sample input
print(find_factors(12)) # Expected output: [1, 2, 3, 4, 6, 12]
print(find_factors(17)) # Expected output: [1, 17]
print(find_factors(36)) # Expected output: [1, 2, 3, 4, 6, 9, 12, 18, 36]
