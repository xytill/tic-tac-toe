numbers = []

while 1:
    numbers.append(int(input()))
    if sum(numbers) == 0:
        break

print(sum(x * x for x in numbers))
