password = input("Enter password: ")
result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False
upper = False
for i in password:
    if i.isdigit():
        digit = True

    if i.isupper():
        upper = True
result.append(digit)
result.append(upper)

if all(result) == True:
    print("Strong password")
else:
    print("Weak password!")