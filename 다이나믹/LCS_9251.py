N = input()
M = input()

dp = [0 for i in range(len(M))]

for i in range(len(N)):
    for j in range(len(M)-1,-1,-1):
        if N[i] == M[j]:
            if dp[:j]!=[]:
                dp[j]=max(dp[:j])+1
            else:
                dp[j]=1
print(max(dp))
