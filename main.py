from art import logo, vs 
print(logo)
import random 
from game_data import data
from replit import clear  # TO clear console between rounds

# Create function which will replace the following A selection with previous B selection   
def to_replace_selection(first_comparison, second_comparison):
  first_person_name = first_comparison['name']
  first_person_description =       first_comparison['description']
  first_person_country = first_comparison['country']
  print(f"Compare A: {first_person_name}, a {first_person_description}, from {first_person_country}.")

  print(vs)
  
  second_comparison = random.choice(data)
  if first_comparison == second_comparison:
    second_comparison = random.choice(data) # To ensure that both comparisons wont be the same -----> comparison B will be regenerated if they both are the same
  second_person_name = second_comparison['name']
  second_person_description =    second_comparison['description']
  second_person_country = second_comparison['country']
  print(f"Compare B: {second_person_name}, a {second_person_description}, from {second_person_country}." )

# below here will be the first comparison

# Create flag variable so that i can end while Loop 
flag_variable = False 
second_flag_variable = False  # Create second flag variable for nested while loop
current_score = 0     # Create global variable which will store the current score
while not flag_variable:    # While True 
  while not second_flag_variable: # While True
    first_selection = random.choice(data)    # Returns rendom element from the list
    first_person_name = first_selection['name']
    first_person_description =       first_selection['description']
    first_person_country = first_selection['country']
    print(f"Compare A: {first_person_name}, a {first_person_description}, from {first_person_country}.")
    
    print(vs)
  #below here will be the second comparison 
    second_selection = random.choice(data)
    if first_selection == second_selection:
      second_selection = random.choice(data) # To ensure that both comparisons wont be the same -----> comparison B will be regenerated if they both are the same
    second_person_name = second_selection['name']
    second_person_description =    second_selection['description']
    second_person_country = second_selection['country']
    print(f"Compare B: {second_person_name}, a {second_person_description}, from {second_person_country}." )
      
    break   # So that while loop will not be infinite-----> break out of while loop
    
# Below here to compare first selection follower_count vs second_selection
  first_person_count = first_selection['follower_count']
  second_person_count = second_selection['follower_count']


#Below here will be to compare using user's input 
  user_selection = input("Who has more followers? Type 'A' or 'B': ").lower()

  if user_selection == 'a' and first_person_count > second_person_count:     # First scenario: Guess correctly that a has more follower counts
    current_score += 1
    clear()  # TO clear console between rounds
    print(logo)  # show logo even in next rounds
    print(f"You are correct. Current score: {current_score}.")   # show previous score even in next round
    second_flag_variable = True # Stop nested while loop
    to_replace_selection(first_comparison = second_selection, second_comparison = first_selection)       # B will become A next comparison 
  
  elif user_selection == 'b' and second_person_count > first_person_count:      # Second scenario: Guess correctly that b has more follower counts
    current_score += 1
    clear()  # TO clear console between rounds
    print(logo)    # show logo even in next rounds
    print(f"You are correct. Current score: {current_score}.")   # show previous score even in next round
    second_flag_variable = True # Stop nested while loop
    to_replace_selection(first_comparison = second_selection, second_comparison = first_selection)        # B will become A next comparison 

  else:
    flag_variable = True  # Ends while loop when guessed wrongly 
    print(f"Sorry that's wrong. Final score: {current_score}")
    
