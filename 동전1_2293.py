n, k = map(int,input().split())

coin = [int(input()) for i in range(n)]
coin = sorted(coin)
dp = [0 for i in range(k + 1)]
for i in range(len(coin)):
    dp[coin[i]] = 1
    
for i in range(coin[0] + 1, k + 1):
    dp[i] += dp[i - coin[0]]
    for j in range(1, len(coin)):
        if i % coin[j] == 0:
            dp[i] += 1
        else:
            print(i, dp)
            break
        
print(dp[-1])
