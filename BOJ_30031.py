n = int(input())
money= 0
for i in range(n):
    w,h = map(int,input().split())
    if w == 136:
        money+=1000
    elif w == 142:
        money+=5000
    elif w == 148:
        money+=10000
    elif w == 154:
        money+=50000

print(money)