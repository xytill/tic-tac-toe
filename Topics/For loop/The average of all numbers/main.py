# put your python code here
a, b = (int(input()) for _ in range(2))
total = 0
count = 0
for i in range(a, b + 1):
    if i % 3 == 0 and (i != (a - 1) or i != (b + 1)):
        total += i
        count += 1

print(total / count)
