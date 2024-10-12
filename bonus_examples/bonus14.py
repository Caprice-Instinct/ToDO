from bonus_examples.converter14 import convert
from bonus_examples.parsers14 import parse

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters.")

if result < 1:
    print("Kid is too short for the slide.")

else:
    print("Kid is tall enough for the slide.")