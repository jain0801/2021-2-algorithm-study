import copy
N, M, V = map(int, input().split())
g = [list(map(int, input().split())) for i in range(M)]

#그래프 그리기
graph = [[False for i in range(N)] for j in range(N)]
for i in range(N):
    graph[i][i] = True
for i in range(len(g)):
    graph[g[i][0] - 1][g[i][1] - 1] = True
    graph[g[i][1] - 1][g[i][0] - 1] = True
graph2 = copy.deepcopy(graph)


def DFS(st):#st는 실제 간선 숫자
    if not (False in visit):
        return None
    for i in range(N):#i는 그래프 접근용. i = st - 1
        if (graph[st - 1][i] == True and visit[i] == False):
            result.append(str(i + 1))
            visit[i] = True
            DFS(i + 1)#st = i + 1

def BFS(st):
    if not (False in visit):
        return None
    tmp = []
    for i in range(N):
        if (graph2[st - 1][i] == True and visit[i] == False):
            result.append(str(i + 1))#간선 숫자 = i + 1
            visit[i] = True #result에 너비우선 탐색 결과넣고 밑에서 다시 이어진 노드탐색
            tmp.append(i + 1)
    for i in range(len(tmp)):
        BFS(tmp[i])

#DFS
visit = [False for i in range(N)] #방문여부
result = [str(V)]
visit[V - 1] = True
DFS(V)
print(' '.join(result))

#BFS
visit = [False for i in range(N)]
result = [str(V)]
visit[V - 1] = True
BFS(V)
print(' '.join(result))
