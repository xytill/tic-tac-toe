cafe_input = []
cafe_list = {}

while 1:
    cafe_input = input().split()
    if "MEOW" in cafe_input:
        print([x for x in cafe_list if cafe_list[x] == max(cafe_list.values())][0])
        break
    else:
        cafe_list[cafe_input[0]] = int(cafe_input[-1])
