integers = [int(x) for x in input()]

print([sum(integers[n:n + 2]) / 2 for n in range(len(integers) - 1)])
