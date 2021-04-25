sentence = input().lower()

sentence = sentence.replace(",", "")
sentence = sentence.replace(".", "")
sentence = sentence.replace("!", "")
sentence = sentence.replace("?", "")

print(sentence)
