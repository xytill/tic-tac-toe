num = int(input())
for x in range(1, num + 1):
    print(" " * (num - x) + "#" * (x + (x - 1)))


base = int(input()) * 2
for i in range(1, base, 2):
    wandax = "#" * i
    print(wandax.center(base))
