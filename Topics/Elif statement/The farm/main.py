money = int(input())

if money >= 6769:
    count = money // 6769
    animal = "sheep"
elif money >= 3848:
    count = money // 3848
    animal = "cow"
elif money >= 1296:
    count = money // 1296
    animal = "pig"
elif money >= 678:
    count = money // 678
    animal = "goat"
elif money >= 23:
    count = money // 23
    animal = "chicken"
else:
    count = 0

if count != 0:
    if animal == "sheep":
        print(count, animal)
    else:
        print(count, animal if count == 1 else animal + "s")
else:
    print("None")
