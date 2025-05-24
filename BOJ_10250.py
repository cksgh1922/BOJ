#호텔의 층수, 호텔의 방수, 몇번째 손님인지 입력받기

n = int(input())

for i in range(n):
    layer,room,okyaku = map(int,input().split())
    
    number = 0
    floor = okyaku%layer
    ho = okyaku//layer + 1 
    
    if floor == 0:
        floor = layer
        ho -= 1
        
    number = floor * 100 + ho
    print(number)   
