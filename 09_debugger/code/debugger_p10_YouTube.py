def like_or_dislike(events):
	state = "like"
	
	for event in range(events):
		if event != state:
			state = "nothing"
		else:
			state = event
	
	return state

# Test the function with a sample input
print(like_or_dislike(["dislike"])) # Expected output: "dislike"
print(like_or_dislike(["like", "like"])) # Expected output: "nothing"
print(like_or_dislike(["dislike", "like"])) # Expected output: "like"
print(like_or_dislike(["like", "dislike", "dislike"])) # Expected output: "nothing"
