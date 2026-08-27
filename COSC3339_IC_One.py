# YOUR NAME HERE
# YOUR SECTION HERE
# DATE OF EDITING HERE

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
    result = side_a + side_b  
    return result

# This method contains a bug. In your commit note, state the bug and how you fixed it
def count_words(sentence):
    if len(sentence) == 0:
        return 0
    words = sentence.split(',')  
    return len(words)


# This method is long to allow for non-overlapping edits.
def calculate_shipping_cost(weight, destination):
    cost = 0.0
    
    if destination == "US":
        base_cost = 5.0
        if weight <= 10:
            cost = base_cost
        else:
            # Over 10 lbs, add $1 per extra lb
            extra_weight = weight - 10
            cost = base_cost + (extra_weight * 1.0)
            
    elif destination == "International":
        base_cost = 15.0
        if weight <= 5:
            cost = base_cost
        else:
            # Over 5 lbs, add $5 per extra lb
            extra_weight = weight - 5
            cost = base_cost + (extra_weight * 5.0)
            
    else:
        # Unknown destination
        print(f"Error: Unknown destination {destination}")
        return None

    return cost


# This method uses funky logic. Rewrite it using different loop structures
def curve_scores(scores):
    return list(map(lambda x: min(x + 5, 100), scores))


# For scenario three change the name of this method.
# For scenario five fix the typos
def _validate_imput(text_value):

    valud_imput = True 
    
    if text_value is None:
        valud_imput = False
    
    if text_value == "":
        valud_imput = False
        
    return valud_imput


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
    
    # print("--- SCENARIO 3 TEST ---")
    # user_input = "This is some fake user data"
    # if process_user_data(user_input):
    #     print("Data processed successfully")
    # else:
    #     print("Data invalid")
    
    print("\n--- END OF TESTS ---")

main()