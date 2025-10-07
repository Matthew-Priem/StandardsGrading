def highway_directions(highway_num):
	if 1 <= highway_num <= 99:
		if highway_num % 2 == 0:
			return f"I-{highway_num} runs north/south"
		else:
			return f"I-{highway_num} runs east/west"


	elif 100 <= highway_num <= 999:
		service_highway = highway_num % 100

		if 1 <= service_highway <= 99:
			if service_highway % 2 == 0:
				return f"I-{highway_num} runs east/west"
			elif service_highway % 2 == 0:
				return f"I-{highway_num} runs north/south"
		else:
			return f"I-{highway_num} is an invalid highway number"
	else:
		return f"I-{highway_num} is an invalid highway number"
	
# Test the function with a sample input

print(highway_directions(5)) # Expected output: "I-5 runs north/south"
print(highway_directions(82)) # Expected output: "I-82 runs east/west"
print(highway_directions(200)) # Expected output: "I-200 is an invalid highway number"
print(highway_directions(353)) # Expected output: "I-353 runs north/south"