factor_number = int(input())
factorial_answer = 1

while factor_number != 1:
    factorial_answer *= factor_number
    factor_number -= 1

print(factorial_answer)
