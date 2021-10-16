N = int(input())
dp = [i for i in range(N + 1)]

for i in range(1, N + 1):
    j = 1
    while i - j*j >= 0:
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        j += 1
print(dp[-1])
