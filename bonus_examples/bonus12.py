feet_inches = input("Enter feet and inches: ")


def parse(feet_inches_arg):
    value = feet_inches_arg.split(" ")
    feet = float(value[0])
    inches = float(value[1])
    return {"feet":feet, "inches":inches}


def convert(feet, inches):
    parse(feet_inches)

    meters = feet * 0.3048 + inches * 0.0254
    return meters


# parsed_feet = parse(feet_inches)["feet"]
# parsed_inches = parse(feet_inches)["inches"]

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters.")

if result < 1:
    print("Kid is too short for the slide.")

else:
    print("Kid is tall enough for the slide.")