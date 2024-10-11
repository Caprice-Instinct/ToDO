password = input("Enter password: ")
result = {}

if len(password) >= 8:
    result["Length"] = True
else:
    result["Length"] = False

digit = False
upper = False
for i in password:
    if i.isdigit():
        digit = True

    if i.isupper():
        upper = True

result["digit"] = digit
result["upper"] = upper

if all(result.values()):
    print("Strong password")
else:
    print("Weak password!")