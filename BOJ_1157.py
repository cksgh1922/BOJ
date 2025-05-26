n = input().upper()

vindo = {}

for char in n:
    if char in vindo:
        vindo[char] += 1
    else:
        vindo[char] = 1

max_count = -1
top = []

for char in vindo:
    if vindo[char] > max_count:
        max_count = vindo[char]
        top.append(char)
    elif vindo[char] == max_count:
        top.append(char)

if len(top) == 1:
    print(top[0])
else:
    print("?")