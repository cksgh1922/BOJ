#입력문
people = int(input())
shirt = list(map(int,input().split()))
shirt_num , pen_num = map(int,input().split())

#셔츠 알고리즘
count = 0
#사이즈별 인원을 셔츠묶음으로 몫을 더하고 나머지가 1이라도 남을경우 1을 추가, 아닐경우는 0을 추가
for char in shirt:
    count += (char//shirt_num) + (1 if char%shirt_num != 0 else 0)
print(count)
#펜 묶음의 개수와 한자루씩 주문하는 개수는 각각 사람을 펜묶음으로 나눈 몫, 나머지 값이다.
print((people//pen_num),(people%pen_num))