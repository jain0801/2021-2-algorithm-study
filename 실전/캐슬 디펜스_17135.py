from itertools import combinations
import copy

N, M, D = map(int, input().split())
castle = [list(map(int, input().split())) for i in range(N)]


#deep = 궁수에서 떨어진 거리
#player = 좌표[i, j]로 표시.
#예외처리 해줘야 함 -> 다른 궁수가 같은 적 공격할 때를 고려안함.(tmp로 처리)
#visit : 턴마다 처리해주는 공격당한 적, v2 : player 탐색때마다 탐색여부 확인
def BFS(player, tmp, visit):
    global D
    deep = 1
    q = [player]
    v = [[False for i in range(M)] for j in range(N)]
    v[player[0]][player[1]] = True
    while q:
        if deep > D:
            return 0
        deep += 1
        for k in range(len(q)):
            i, j = q.pop(0)
            if castle[i][j] == 1 and visit[i][j] == False:
                if tmp[i][j] == False:
                    tmp[i][j] = True
                    return 1
                else:
                    return 0
            if j > 0 and v[i][j - 1] == False:
                v[i][j - 1] = True
                q.append([i, j - 1])
            if i > 0 and v[i - 1][j] == False:
                v[i - 1][j] = True
                q.append([i - 1, j])
            if j < M - 1 and v[i][j + 1] == False:
                v[i][j + 1] = True
                q.append([i, j + 1])
    return 0
    

#p1, p2, p3는 궁수들 위치
def play(p1, p2, p3):
    cnt = 0
    visit = [[False for i in range(M)] for j in range(N)]
    tmp = [[False for i in range(M)] for j in range(N)]
    for i in range(N):
        p1[0] -= 1
        cnt += BFS(p1, tmp, visit)
        p2[0] -= 1
        cnt += BFS(p2, tmp, visit)
        p3[0] -= 1
        cnt += BFS(p3, tmp, visit)
        visit = copy.deepcopy(tmp) #여기서 deepcopy 안해서 오류남.
    return cnt

#궁수를 어디로 배치할지
comb = list(combinations([i for i in range(M)], 3))
ls = []
for i in range(len(comb)):
    ls.append(play([N, comb[i][0]],[N, comb[i][1]],[N, comb[i][2]]))
print(max(ls))
