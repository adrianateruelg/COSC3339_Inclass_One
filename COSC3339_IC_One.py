# Adriana Teruel
# COSC-3339-01
# August 27, 2026

"""
ASSIGNMENT: INTRODUCTION TO MERGING
-----------------------------------
This file contains several methods with logical errors, poor style, 
and complex constructs. Your goal is to fix them across multiple 
branches to simulate merge conflicts.
"""

import math

# This method contains a bug. In your commit note, state the bug and how you fixed it
def calculate_hypotenuse(side_a, side_b):
	result = math.sqrt(side_a**2 + side_b**2)  
	return result

# This method contains a bug. In your commit note, state the bug and how you fixed it
def count_words(sentence):
	if len(sentence) == 0:
		return 0
	words = sentence.split()  
	return len(words)


# This method is long to allow for non-overlapping edits.
def calculate_shipping_cost(weight, destination):
	cost = None # Change 1: was 0.0, now None 
	
	if destination == "US":
		flat_rate = 5.0 # Change 2: renamed base_cost to flat_RATE
		if weight <= 15: # Change 3: changed weight from 10 to 15
			cost = flat_rate
		else:
			# Over 10 lbs, add $1 per extra lb
			extra_weight = weight - 10
			cost = flat_rate + (extra_weight * 1.0)
			
	elif destination == "International":
		base_cost = 20.0 #Change 1: changed base_cost to 20.0
		if weight <= 5:
			cost = base_cost
		else:
			# Over 5 lbs, add $5 per extra lb
			extra_weight = weight - 5
			cost = base_cost + (extra_weight * 5.0)
			
	else:
		# Unknown destination
		print(f"Error: Unknown destination {destination}")
		return -1 #Change 2: returning -1 instead of None

	return round(cost,2) #Change 3: return rounded to two decimal places


# This method uses funky logic. Rewrite it using different loop structures
def curve_scores(scores):
	CURVE_MULTIPLIER = 1.05
	curved = []
	for score in scores:
		curved.append(min(score * CURVE_MULTIPLIER, 100))
	return curved


# For scenario three change the name of this method.
# For scenario five fix the typos
def _validate_imput_field(text_value): #renamed to _validate_input_field

	valud_imput = True 
	
	if text_value is None:
		valud_imput = False
	
	if text_value == "":
		valud_imput = False
		
	return valud_imput

def process_user_data(user_input):
	if _validate_imput_field(user_input): 
		print(f"Processing: {user_input}")
		return True
	else:
		return False


def main():
	print("--- STARTING TESTS ---")

	# TEST A: Hypotenuse
	print(f"Test A1 (0, 5): {calculate_hypotenuse(0, 5)} (Expected: 5.0)") 
	print(f"Test A2 (3, 4): {calculate_hypotenuse(3, 4)} (Expected: 5.0)") 

	print("-" * 20)

	# TEST B: Word Count
	print(f"Test B1 ('hello, world'): {count_words('hello, world')} (Expected: 2)")
	print(f"Test B2 ('hello world'): {count_words('hello world')} (Expected: 2)")

	print("-" * 20)

	# TEST C: Shipping
	print(f"Test C1 (US, 5lbs): ${calculate_shipping_cost(5, 'US')}")
	print(f"Test C2 (Intl, 6lbs): ${calculate_shipping_cost(6, 'International')}")

	print("-" * 20)

	# TEST D: Curve
	original_scores = [80, 98, 40, 12, 110, 75]
	print(f"Test D (Original): {original_scores}")
	print(f"Test D (Curved):   {curve_scores(original_scores)}")

	print("-" * 20)

	# SCENARIO 3 TEST BLOCK
	# INSTRUCTIONS: 
	# In 'Change Six', you will uncomment the lines below and write 
	# a new function called 'process_user_data' that uses the helper.
	
	print("--- SCENARIO 3 TEST ---")
	user_input = "This is some fake user data"
	if process_user_data(user_input):
		print("Data processed successfully")
	else:
		print("Data invalid")
	
	print("\n--- END OF TESTS ---")

main()