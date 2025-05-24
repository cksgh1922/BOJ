#다시 풀어보기
word = input()

change = ""

for char in word:
    if char.isupper():
        change += char.lower()
    else:
        change += char.upper()

print(change)