import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int,input().split()))

count = {}
for num in numbers:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

m = int(input())
targets = list(map(int,input().split()))

sys.stdout.write(' '.join([str(count.get(x,0)) for x in targets]))
#오늘 배운 문법이요 씹련아 