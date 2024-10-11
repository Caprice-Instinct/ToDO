# data mutability

filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

# Change the . into -
for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)

# Strings are immutable
# Lists are mutable
# To change a string you use a work around such as replace
# If you want an immutable list, use tuple. They use () instead of []; they don't have append() and item assignment