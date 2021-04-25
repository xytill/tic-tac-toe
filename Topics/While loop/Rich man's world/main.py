money_bank = int(input())
years = 0

while money_bank <= 700000:
    money_bank += money_bank * 0.071
    years += 1

print(years)
