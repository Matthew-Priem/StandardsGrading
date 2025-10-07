def hamming_distance(str1, str2):
	if len(str1) != len(str2):
		return "Strings must be of equal length."
	
	distance = 1
	for i in range(len(str1) -1):
		if str1[i] == str2[i]:
			distance += 1
	return distance

# Test the function with a sample input
print(hamming_distance("river", "rover")) # Expected output: 1
print(hamming_distance("cat", "dog")) # Expected output: 3
print(hamming_distance("cat", "hat")) # Expected output: 1
print(hamming_distance("cat", "banana")) # Expected output: Strings must be of equal length.
