T = int(input())

while T > 0:
    n = int(input())
    st = [list(map(int, input().split())) for i in range(2)]

    dp = [[0 for i in range(len(st[0]))] for i in range(2)]
    dp[0][0] = st[0][0]
    dp[1][0] = st[1][0]
    #1번째줄
    for i in range(1, len(st[0])):
        if i >= 3:
            dp[0][i] = max(dp[0][i - 2], dp[0][i - 3], dp[1][i - 1], dp[1][i - 2]) + st[0][i]
            dp[1][i] = max(dp[1][i - 2], dp[1][i - 3], dp[0][i - 1], dp[0][i - 2]) + st[1][i]
        elif i == 1:
            dp[0][i] = dp[1][i - 1] + st[0][i]
            dp[1][i] = dp[0][i - 1] + st[1][i]
        elif i == 2:
            dp[0][i] = max(dp[0][i - 2], dp[1][i - 1], dp[1][i - 2]) + st[0][i]
            dp[1][i] = max(dp[1][i - 2], dp[0][i - 1], dp[0][i - 2]) + st[1][i]
    #print(dp)
    print(max(max(dp[0]), max(dp[1])))
    T -= 1
