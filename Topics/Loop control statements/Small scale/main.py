minimum_number = 99999

while 1:
    number = input()
    if number == ".":
        break
    minimum_number = float(number) if float(number) < minimum_number else minimum_number

print(minimum_number)
