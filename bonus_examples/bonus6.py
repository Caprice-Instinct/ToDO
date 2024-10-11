contents = ["All carrots are sliced "
            "longitudinally",
            "But the carrots were supposedly sliced",
            "The slicing process was so brutal"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)
    file.close()

long_string = "I am a very long string " \
    "with many characters"

print(long_string)