n = int(input())
check_num = 0

for _ in range(n):
    check_num = int(input())
    if check_num % 7 == 0:
        print(check_num ** 2)
