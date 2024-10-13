import json

with open("questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, alt in enumerate(question["alts"]):
        print(f"{index + 1}.{alt}")
    user_answer = int(input("Enter your answer:"))
    question["user_answer"] = user_answer

score = 0

for index, question in enumerate(data):
    if question["user_answer"] == question["correct_answer"]:
        score += 1
        result = "Correct answer"
    else:
        result = "Wrong answer"
    message = f"{index + 1}. {result}. Your answer: {question['user_answer']}, " \
              f"Correct answer: {question['correct_answer']}"
    print(message)
print(score, "/", len(data))
