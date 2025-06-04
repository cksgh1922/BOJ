N,K = map(int,input().split())
N_Factorial = 1
K_Factorial = 1
N_K_Factorial = 1
for i in range(N,0,-1):
    N_Factorial*=i
for j in range(K,0,-1):
    K_Factorial*=j
for k in range((N-K),0,-1):
    N_K_Factorial*=k

print((N_Factorial)//(K_Factorial*N_K_Factorial))
#(N)     
#(K) = N!/K!(N-K)!