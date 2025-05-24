#버블 정렬 알고리즘 꼭 알기 

while True:
    triangle = list(map(int,input().split()))
    
    if triangle[0] == 0 and triangle[1] == 0 and triangle[2] == 0:
        break
    for i in range(len(triangle)):
        for j in range(len(triangle)-1 - i):
            if triangle[j] < triangle[j+1]:
                triangle[j],triangle[j+1] = triangle[j+1],triangle[j]
            
    if triangle[0]**2 == (triangle[1])**2 + (triangle[2])**2:
        print("right")
    else:
        print("wrong")
     
    