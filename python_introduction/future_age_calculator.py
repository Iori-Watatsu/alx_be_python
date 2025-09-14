# This takes user input and calculates their future age.

# These variables prompts for user's age input and sets the current and future year being calucated.
current_age = int(input("How old are you? " ))
current_year = 2023
future_year = 2050

# This variable calulates the future age from current age.
age = future_year - current_year + current_age

# Print the user's furture age.
print("In 2050, you will be", age, "years old." )
