calculation_to_units = 24 * 60 * 60
name_of_unit = "seconds"


def days_to_units(num_of_days):
    # print(type(num_of_days > 0))
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
     #if user_input.isdigit():
    try :
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
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
    user_input = input("Enter the no of days you want to convert:\n")
    # print(type(user_input.split(", ")))
    # print(user_input.split(", "))
    for num_of_days_element in set(user_input.split(", ")):
        validate_and_execute()


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