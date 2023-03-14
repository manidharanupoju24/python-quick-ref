from helper import validate_and_execute, user_input_message
import os

user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    # print(type(user_input.split(", ")))
    # print(user_input.split(", "))
    list_of_days = user_input.split(":") # splits into 2 values into a list
    print(list_of_days)
    print(os.name)
    days_and_unit_dictionary = {"days": list_of_days[0], "unit": list_of_days[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute(days_and_unit_dictionary)
    """
      for num_of_days_element in set(list_of_days):
        validate_and_execute()
    """



#print("20 days are " + str(20 * 24 * 60) + " minutes")
#print(f"20 days are {20 * 24 * 60} minutes")
#print(f"35 days are {35 * 24 * 60} minutes")
#print(f"50 days are {50 * 24 * 60} minutes")
#print(f"50 days are {50 * calculation_to_units} {name_of_unit}")
#print(f"110 days are {110 * calculation_to_units} {name_of_unit}")

"""
This is multiline comment
sample
"""

"""
some of the built in functions
print() = prints to the standard output device
input() = asks user for input
split() = takes in a special char and splits the text from it 
set() = returns a new set for. e.g. converts a list to int
*** each datatype has its own set of built in functions ***
"""

"""
datatypes : 
Integers
strings
float
boolean
lists
sets
dictionaries
"""