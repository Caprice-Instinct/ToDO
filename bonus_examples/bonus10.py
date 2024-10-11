while True:
    try:
        width = float(input("Width: "))
        length = float(input("Length: "))

        if width == length:
            exit("Isn't that a square?")

        area = width * length
        print(f"Area is {area}")
        break

    except ValueError:
        print("Please enter a number.")