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


def validate_and_execute(days_and_unit_dictionary):
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


user_input_message = "Enter the no of days you want to convert, along with the conversion unit:\n"