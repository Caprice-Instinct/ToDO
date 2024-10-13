def parse(feet_inches_arg):
    value = feet_inches_arg.split(" ")
    feet = float(value[0])
    inches = float(value[1])
    return {"feet":feet, "inches":inches}
