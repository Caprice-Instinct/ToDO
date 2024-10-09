# Infinite loop
while True:
    print("Hello")

# Declare variables once to reduce a lot of execution; makes the program heavier
user_prompt = "Enter a todo: "
todos = []

while True:
    todo = input(user_prompt)
    # title() method capitalises the first letter of all words
    # removing the () from methods returns the type which is method; no output
    todos.append(todo.title())
    print(todos)