#유클리드 호제법 : 두수 a,b의 최대공약수는 b와 a%b의 최대공약수와 같다.
def choiso(a,b):
    while b != 0:
        a,b = b, a%b
    return a

#최소공배수는 두 수의 곱을 최대공약수로 나눈 것
def choidai(a,b):
    return a*b // choiso(a,b)

n,m = map(int,input().split())

print(choiso(n,m))
print(choidai(n,m))