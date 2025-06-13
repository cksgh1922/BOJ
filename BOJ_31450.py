import sys
m, k = map(int, sys.stdin.readline().split())
print("Yes" if m % k == 0 else "No")