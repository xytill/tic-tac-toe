scores = input().split()

incorrect_answers = scores.count("I")
last_fail = len(scores)

if incorrect_answers < 3:
    print("You won")
else:
    print("Game over")
    last_fail = [i for i, val in enumerate(scores) if val == "I"][2] + 1

print(scores[:last_fail].count("C"))
