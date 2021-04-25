get_numbers = [int(x) for x in list(input())]
new_numbers = [sum(get_numbers[:x]) for x in range(1, len(get_numbers) + 1)]
print(new_numbers)
