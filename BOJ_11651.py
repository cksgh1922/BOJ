import sys

n = int(sys.stdin.readline())

matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

matrix.sort(key=lambda x: (x[1],x[0]))

for item in matrix:
    sys.stdout.write(' '.join(map(str,item))+'\n')
