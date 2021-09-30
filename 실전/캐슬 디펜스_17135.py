from itertools import combinations
import copy

N, M, D = map(int, input().split())
castle = [list(map(int, input().split())) for i in range(N)]


#deep = 궁수에서 떨어진 거리
#player = 좌표[i, j]로 표시.
#예외처리 해줘야 함 -> 다른 궁수가 같은 적 공격할 때를 고려안함.(tmp로 처리)

def BFS(player, tmp):
    global D
    deep = 1
    q = [player]
    v2 = [[False for i in range(M)] for i in range(N)]
    while q:
        if deep > D:
            return 0
        deep += 1
        for k in range(len(q)):
            i, j = q.pop(0)
            if castle[i][j] == 1 and visit[i][j] == False:
                tmp[i][j] = True
                return 1
            if j > 0 and v2[i][j - 1] == False:
                v2[i][j - 1] = True
                q.append([i, j - 1])
            if i > 0 and v2[i - 1][j] == False:
                v2[i - 1][j] = True
                q.append([i - 1, j])
            if j < M - 1 and v2[i][j + 1] == False:
                v2[i][j + 1] = True
                q.append([i, j + 1])
    

#p1, p2, p3는 궁수들 위치
def play(p1, p2, p3):
    cnt = 0
    global visit
    tmp = copy.deepcopy(visit)
    for i in range(N):
        p1[0] -= 1
        cnt += BFS(p1, tmp)
        p2[0] -= 1
        cnt += BFS(p2, tmp)
        p3[0] -= 1
        cnt += BFS(p3, tmp)
        visit = tmp
    return cnt

#궁수를 어디로 배치할지
comb = list(combinations([i for i in range(M)], 3))
ls = []
for i in range(len(comb)):
    visit = [[False for i in range(M)] for i in range(N)]
    ls.append(play([N, comb[i][0]],[N, comb[i][1]],[N, comb[i][2]]))
print(max(ls))

