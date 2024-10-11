names = ["Lisa", "kendi", "reuben", "Amani"]
names.sort()

for index, name in enumerate(names):
    row = f"{index + 1}.{name.capitalize()}"
    print(row)

print("\n")

names.sort(reverse=True)

for index, name in enumerate(names):
    row = f"{index + 1}.{name.capitalize()}"
    print(row)