string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
count_vowels = 0

for x in string:
    if x in vowels:
        count_vowels += 1

print(count_vowels)
