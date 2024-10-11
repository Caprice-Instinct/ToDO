prompt = "Enter a new member: "

file = open(f"../files/members.txt", 'r')
members = file.readlines()
file.close()
new_member = input(prompt)
members.append(new_member + "\n")


file = open(f"../files/members.txt", 'w')
file.writelines(members)
file.close()