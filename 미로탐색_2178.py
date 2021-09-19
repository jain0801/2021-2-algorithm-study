N, M = map(int, input().split())
graph = [list(input()) for i in range(N)]

#초기설정
visit = [[False for i in range(M)] for i in range(N)]
visit[0][0] = True

#너비우선 탐색
q = [[0, 0, 1]]
def BFS(): #s1 = N, s2 = M
    while q:
        for i in q:
            s1, s2, deep = q.pop(0)
            if s1 == N - 1 and s2 == M - 1:
                return deep
            if s2 - 1 >= 0:
                if graph[s1][s2 - 1] == "1" and visit[s1][s2 - 1] == False: #왼쪽탐색
                    q.append([s1, s2 - 1, deep + 1])
                    visit[s1][s2 - 1] = True
            if s2 + 1 < M:
                if graph[s1][s2 + 1] == "1" and visit[s1][s2 + 1] == False: #오른쪽탐색
                    q.append([s1, s2 + 1, deep + 1])
                    visit[s1][s2 + 1] = True
            if s1 - 1 >= 0:
                if graph[s1 - 1][s2] == "1" and visit[s1 - 1][s2] == False: #위탐색
                    q.append([s1 - 1, s2, deep + 1])
                    visit[s1 - 1][s2] = True
            if s1 + 1 < N:
                if graph[s1 + 1][s2] == "1" and visit[s1 + 1][s2] == False: #아래탐색
                    q.append([s1 + 1, s2, deep + 1])
                    visit[s1 + 1][s2] = True

print(BFS())
