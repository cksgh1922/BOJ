n = int(input())
name_list = [input().split() for val in range(n)]


sorted_age = sorted(name_list, key=lambda x: int(x[0]))

for item in sorted_age:
    print(" ".join(item))