import copy
N = int(input())
gr = [list(map(int, input().split())) for i in range(N)]

"""
sudo 코드

깊이우선 알고리즘 활용
위, 아래, 오른쪽, 왼쪽을 움직이는 경우의 수를 모두 탐색.
깊이가 최대까지 갔으면 뒤로 가서 가지 않은 경우의 수 탐색.

움직일 때 고려해야 할 사항
- 옮겨지는 숫자가 같으면 합치고, 같지 않으며 합치지 않음.

상하좌우로 움직이는 경우의 수를 하나의 알고리즘으로 만들 수 있을까?
nxm 블록이라 가정할 때
-오른쪽으로 움직일 때는 오른쪽에 있는 블록부터 시작해서 왼쪽으로 이동
:m[N]부터 m[0]까지
-왼쪽으로 움직일 때
:m[0]부터 m[N]까지
-위쪽으로
:n[0]부터 n[N]까지
-아래쪽으로
:n[N]부터 n[0]까지
-->>> 매개변수로 좌우/위아래인지 + 0부터 시작인지 N부터 시작인지 정해주면 됨.
-->>> 위아래인지 좌우인지만 나누면 될듯.

움직이는 경우
1. 해당 칸 위가 0이면 위로 계속 이동
2. 위아래가 같은 숫자면 움직이는 방향 숫자 *2 밑에는 0
"""

mx = []
#g는 그래프
def move(deep, g):
    #위
    global N
    if deep > 5:
        mx.append(max(map(max, g)))
        return None
    up = copy.deepcopy(g)
    for j in range(N):
        check = -1 #합쳐진 부분이 있는 곳
        for i in range(N):
            if up[i][j] == 0:#해당칸 0이면 패스
                continue
            k = 0
            for k in range(i):#위가 0(빈칸)이 아닐때까지 옮김
                if up[i - (k + 1)][j] != 0:
                    t = k
                    break
                up[i - k][j], up[i - (k + 1)][j] = up[i - (k + 1)][j], up[i - k][j]
            #현재 위치는 up[i - k][j]
            #위의 인덱스가 0이상이고, 위에 인덱스가 합쳐졌던 곳이 아니고, 위랑 현재랑 값 같을 때
            #값을 합침.
            if i - k - 1 >= 0 and i - k - 1 != check and up[i - k][j] == up[i - k - 1][j]:
                up[i - k - 1][j] *= 2
                up[i - k][j] = 0
                check = i - k - 1
            

    #왼쪽
    left = copy.deepcopy(g)
    for i in range(N):
        check = -1 #합쳐진 부분이 있는 곳
        for j in range(N):
            if left[i][j] == 0:#해당칸 0이면 패스
                continue
            for k in range(j):#위가 0(빈칸)이 아닐때까지 옮김
                if left[i][j - (k + 1)] != 0:
                    break
                left[i][j - k], left[i][j - (k + 1)] = left[i][j - (k + 1)], left[i][j - k]
            #위의 인덱스가 0이상이고, 위에 인덱스가 합쳐졌던 곳이 아니고, 위랑 현재랑 값 같을 때
            #값을 합침.
            if j - k - 1 >= 0 and j - k - 1 != check and left[i][j - k] == left[i][j - k - 1]:
                left[i][j - k - 1] *= 2
                left[i][j - k] = 0
                check = j - k - 1
          
    #아래
    down = copy.deepcopy(g)
    for j in range(N):
        check = N #합쳐진 부분이 있는 곳
        for i in range(N - 1, -1, -1):
            if down[i][j] == 0:#해당칸 0이면 패스
                continue
            for k in range(N - i - 1):#위가 0(빈칸)이 아닐때까지 옮김
                if down[i + (k + 1)][j] != 0:
                    break
                down[i + k][j], down[i + (k + 1)][j] = down[i + (k + 1)][j], down[i + k][j]
            #위의 인덱스가 0이상이고, 위에 인덱스가 합쳐졌던 곳이 아니고, 위랑 현재랑 값 같을 때
            #값을 합침.
            if i + k + 1 < N and i + k + 1 != check and down[i + k][j] == down[i + k + 1][j]:
                down[i + k + 1][j] *= 2
                down[i + k][j] = 0
                check = i + k + 1


    #오른쪽
    right = copy.deepcopy(g)
    for i in range(N):
        check = N #합쳐진 부분이 있는 곳
        for j in range(N - 1, -1, -1):
            if right[i][j] == 0:#해당칸 0이면 패스
                continue
            for k in range(N - j - 1):#위가 0(빈칸)이 아닐때까지 옮김
                if right[i][j + (k + 1)] != 0:
                    break
                right[i][j + k], right[i][j + (k + 1)] = right[i][j + (k + 1)], right[i][j + k]
            #위의 인덱스가 0이상이고, 위에 인덱스가 합쳐졌던 곳이 아니고, 위랑 현재랑 값 같을 때
            #값을 합침.
            if j + k + 1 < N and j + k + 1 != check and right[i][j + k] == right[i][j + k + 1]:
                right[i][j + k + 1] *= 2
                right[i][j + k] = 0
                check = j + k + 1

    move(deep + 1, up)
    move(deep + 1, down)
    move(deep + 1, left)
    move(deep + 1, right)

move(1, gr)
print(max(mx))
