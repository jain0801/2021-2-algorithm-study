N = int(input())
M = int(input())

graph = [[False for i in range(N)] for i in range(N)]
visit = [False for i in range(N)]
for k in range(M):
    i, j = map(int, input().split())
    graph[i - 1][j - 1] = True
    graph[j - 1][i - 1] = True

cnt = 0
def DFS(st):
    global cnt
    for i in range(N):
        if graph[st][i] == True and visit[i] == False:
            visit[i] = True
            cnt += 1
            DFS(i)

DFS(0)
print(cnt - 1)
