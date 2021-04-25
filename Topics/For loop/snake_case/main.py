word = list(input())
cnt = 0

for x in word:
    if x.isupper() and cnt != 0:
        word[cnt] = "_" + x
    cnt += 1

print(("".join(map(str, word))).lower())
