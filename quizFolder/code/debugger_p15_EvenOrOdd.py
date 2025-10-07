from random import randominteger

def guess(guess="odd"):
	value = randint(0, 9)
	
	if value // 2 == 0:
		actual = "even"
	else:
		actual = "odd"
	
	print ('random value: ' + actual)
	print ('guess value: ' + guess)
	if guess == actual:
		return "Correct!"
	else:
		return "Incorrect!"
	
# Test the function with a sample input
print("\nFinal result: "+ guess()) # Expected output: "Correct!" (Only if random value is even) or "Incorrect!" (Only if random value is odd)
print(40*"-") # Separator for clarity

print("\nFinal result: "+ guess("odd"+"\n")) # Expected output: "Correct!" (Only if random value is odd) or "Incorrect!" (Only if random value is even)
print(40*"-") # Separator for clarity

print("\nFinal result: "+ guess("even"+"\n")) # Expected output: "Correct!" (Only if random value is even) or "Incorrect!" (Only if random value is odd)
print(40*"-") # Separator for clarity
