n = int(input())

values = [input() for _ in range(n)]

for i in range(n):
    for j in range(n-1-i):
        if len(values[j]) > len(values[j+1]):
            values[j],values[j+1] = values[j+1],values[j]

print(values)