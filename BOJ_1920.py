n = int(input())
A = set(map(int,input().split()))

M = int(input())
B = list(map(int,input().split()))

for x in B:
    print(1 if x in A else 0)

#set은 값을 어떤 수학적 공식인 해시 함수로 바꿔서 그 숫자를 인덱스로 써서 배열처럼 바로 접근
#리스트와는 다름. list[i]부터 [n]까지 하나하나 확인한다면, set은 x in A 에서 x 값을 변환시켜
#바로 확인함.