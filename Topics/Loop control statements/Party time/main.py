guests = []

while 1:
    guest = input()
    if guest == ".":
        print(guests)
        print(len(guests))
        break
    else:
        guests.append(guest)
