tally = [input().split(" ") for _ in range(int(input()))]
print([winner[0] for winner in tally if winner[1] == "win"])
print(sum([1 for winner in tally if winner[1] == "win"]))
