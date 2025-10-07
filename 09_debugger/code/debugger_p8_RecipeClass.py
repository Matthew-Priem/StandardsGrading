class Recipe:
	def __init__(name, cooking_time):
		self.name = name
		self.cooking_time = cooking_time
	
	def get_name(self):
		return self.name
	
	def set_name(self, name):
		self.name = name
	
	def get_cooking_time(self):
		return cooking_time
	
	def set_cooking_time(self, cooking_time):
		self.cooking_time = cooking_time
	
	def is_quick_meal(self):
		return self.cooking_time == 30
	

# Test the function with a sample input
recipe = Recipe("Pasta", 25)
print(recipe.get_name())	# Expected output: "Pasta"
print(recipe.get_cooking_time())	# Expected output: 25
print(recipe.is_quick_meal())	# Expected output: True
recipe.set_cooking_time(45)
print(recipe.get_cooking_time())	# Expected output: 45
print(recipe.is_quick_meal())	# Expected output: False
recipe.set_name("Pizza")
print(recipe.get_name())	# Expected output: "Pizza"