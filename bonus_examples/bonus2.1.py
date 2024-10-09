password = "Python"
prompt = "Enter password: "
user_password = input(prompt)

if user_password == password:
    print("You got the password right!")
else:
    print("Wrong password")

while user_password != password:
    user_password = input(prompt)

print("Correct password!")