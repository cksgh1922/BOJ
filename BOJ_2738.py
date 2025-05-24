#다시 풀어보기
n , m = map(int,input().split())

first_matrix = []
second_matrix = []

for i in range(n):
    row = list(map(int,input().split()))
    first_matrix.append(row)

for i in range(n):
    row = list(map(int,input().split()))
    second_matrix.append(row)
    
sum_matrix = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(first_matrix[i][j] + second_matrix[i][j])
    sum_matrix.append(row)
    
for i in range(n):
    print(*sum_matrix[i])