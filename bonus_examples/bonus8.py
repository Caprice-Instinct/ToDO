date_prompt = "Enter today's date: "
date = input(date_prompt)
mood_prompt = "Rate your mood on a scale of 1 to 10: "
mood = input(mood_prompt)
thoughts_prompt = "Let your thoughts flow: \n"
thoughts = input(thoughts_prompt)

with open(f"../journal/{date}.txt", 'w') as file:
    file.write(mood + 2*"\n")
    file.write(thoughts)