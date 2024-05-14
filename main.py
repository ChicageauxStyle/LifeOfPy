calculation_to_units = input("Would you like to convert to hours or minutes? ").lower()

if calculation_to_units == "hours":
    conversion_factor = 24
    name_of_unit = "hours"
elif calculation_to_units == "minutes":
    conversion_factor = 24*60
    name_of_unit = "minutes"
else:
    print("Invalid input. Please enter 'hours" or 'minutes')
    exit()

#calculation_to_units = 24
#name_of_unit = "hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * conversion_factor} {name_of_unit}"

def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(f"{user_input_number} days are {calculated_value}")
            
        elif user_input_number == 0:
            print("You entered 0. Please enter a positive value")
    else:
        print("Value not a valid number. Unable to run program!")

user_input = input(f"Hey user, enter a number of days and I will convert it to {name_of_unit}!\n")
validate_and_execute()



