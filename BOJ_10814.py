n = int(input())
name_list = [input().split() for val in range(n)]


sorted_age = sorted(name_list, key=lambda x: int(x[0]))

for item in sorted_age:
    print(" ".join(item))
    
    #join이 여기서는 list안의 list에서 (2차원리스트) 각 원소들을 묶을 때 사용됨.