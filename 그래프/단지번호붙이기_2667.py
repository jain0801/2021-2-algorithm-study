N = int(input())
m = [list(map(int, input())) for i in range(N)]
M = len(m[0])
visit = [[False for i in range(len(m[0]))] for i in range(N)]

         
total = 0
def BFS(I, J):
    cnt = 0
    q = [[I, J]]
    while q:
        for k in range(len(q)):
            i, j = q.pop(0)
            cnt += 1
            if i > 0: #위 탐색
                if m[i - 1][j] == 1 and visit[i - 1][j] == False:
                    visit[i - 1][j] = True
                    q.append([i - 1, j])
            if i < N - 1: #아래 탐색
                if m[i + 1][j] == 1 and visit[i + 1][j] == False:
                    visit[i + 1][j] = True
                    q.append([i + 1, j])
            if j > 0: #왼쪽 탐색
                if m[i][j - 1] == 1 and visit[i][j - 1] == False:
                    visit[i][j - 1] = True
                    q.append([i, j - 1])
            if j < M - 1: #위 탐색
                if m[i][j + 1] == 1 and visit[i][j + 1] == False:
                    visit[i][j + 1] = True
                    q.append([i, j + 1])
        
    return cnt - 1

cnt_list = []
for i in range(N):
    for j in range(M):
        if m[i][j] == 1 and visit[i][j] == False:
            total += 1
            cnt_list.append(BFS(i, j))

cnt_list.sort()
print(total)
for i in range(len(cnt_list)):
    print(cnt_list[i])
