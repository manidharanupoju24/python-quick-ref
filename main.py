calculation_to_hours = 24
calculation_to_minutes = calculation_to_hours * 60
calculation_to_seconds = calculation_to_minutes * 60


def days_to_units(num_of_days, conversion_unit):
    # print(type(num_of_days > 0))
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * calculation_to_hours} {conversion_unit}"
    elif conversion_unit == "seconds":
        return f"{num_of_days} days are {num_of_days * calculation_to_seconds} {conversion_unit}"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * calculation_to_minutes} {conversion_unit}"
    else:
        return "Unsupported Unit"


def validate_and_execute():
     #if user_input.isdigit():
    try :
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0 :
            print("You entered 0 days. Enter atleast one positive number to calculate.")
        else:
            print("You entered a negative number, please enter a valid positive number")
     #else :
    except ValueError:
        print("Your input is not a number! Don't ruin my program")


user_input = ""
while user_input != "exit":
    user_input = input("Enter the no of days you want to convert, along with the conversion unit:\n")
    # print(type(user_input.split(", ")))
    # print(user_input.split(", "))
    list_of_days = user_input.split(":") # splits into 2 values into a list
    print(list_of_days)
    days_and_unit_dictionary = {"days": list_of_days[0], "unit": list_of_days[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute()
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