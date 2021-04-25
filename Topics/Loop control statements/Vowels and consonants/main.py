check_word = input().lower()

for n in check_word:
    if not n.isalpha():
        break
    elif n in ("a", "e", "i", "o", "u"):
        print("vowel")
    else:
        print("consonant")
