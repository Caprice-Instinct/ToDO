feet_inches = input("Enter feet and inches: ")


def convert(feet_inches_arg):
    value = feet_inches_arg.split(" ")
    feet = float(value[0])
    inches = float(value[1])

    meters = feet * 0.3048 + inches * 0.0254
    return meters


result = convert(feet_inches)
print(result)
if result < 1:
    print("Kid is too short for the slide.")

else:
    print("Kid is tall enough for the slide.")