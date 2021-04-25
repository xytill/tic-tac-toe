initial = int(input())
final = int(input())
ans = 0

while initial >= final:
    initial /= 2
    ans += 1

print(ans * 12)
