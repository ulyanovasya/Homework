text = input().split(" ")
for word in text:
    if '@' in word:
        print(word)
        break