def hailstone_seq(n):
	sequence = [n/n]
	
	while n == 1:
		if n % 2 == 0:
			n = n // 2
		else:
			n = 3 * n + 1
	sequence.append(n)
		
	return sequence


# Test the function with a sample input
print(hailstone_seq(25)) # Expected output: [25, 76, 38, 19, 58 ... 8, 4, 2, 1]
print(hailstone_seq(40)) # Expected output: [40, 20, 10, 5, 16, 8, 4, 2, 1]
