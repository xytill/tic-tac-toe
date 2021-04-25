score, maximum = (float(input()) for _ in range(2))
percentage = (score / maximum) * 100

if percentage >= 90:
    print("A")
elif percentage >= 80:
    print("B")
elif percentage >= 70:
    print("C")
elif percentage >= 60:
    print("D")
else:
    print("F")
