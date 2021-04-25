# put your python code here
duration = int(input())
food_cost = duration * int(input())
flight_cost = 2 * int(input())
night_cost = (duration - 1) * int(input())

print(food_cost + flight_cost + night_cost)
