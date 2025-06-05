import sys

n,m = map(int,sys.stdin.readline().split())

listend = set(sys.stdin.readline().strip() for _ in range(n))
saw = set(sys.stdin.readline().strip() for _ in range(m))

#이코드는 두 집합의 교집합을 따로 정리하는 함수이다.
common = sorted(listend&saw)

sys.stdout.write(f"{len(common)}'\n'{'\n'.join(common)}")