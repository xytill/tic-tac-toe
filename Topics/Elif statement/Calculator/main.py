# put your python code here
first_num, second_num = (float(input()) for _ in range(2))
operation = input()

if second_num == 0.0 and operation in ["mod", "/", "div"]:
    print("Division by 0!")
else:
    if operation == "+":
        print(float(first_num + second_num))
    elif operation == "-":
        print(float(first_num - second_num))
    elif operation == "/":
        print(float(first_num / second_num))
    elif operation == "*":
        print(float(first_num * second_num))
    elif operation == "mod":
        print(float(first_num % second_num))
    elif operation == "pow":
        print(float(first_num ** second_num))
    elif operation == "div":
        print(float(first_num // second_num))
