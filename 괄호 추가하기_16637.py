from itertools import combinations
from functools import reduce

def cal(i, j, k):#i는 n번째 있는 수식어인지, j앞에숫자, k는 뒤에 숫자
    if (ls[i] == '+'):
        return j + k
    if (ls[i] == '-'):
        return j - k
    if (ls[i] == '*'):
        return j * k
    
N = int(input())
ls = list(input())

#1, 2개짜리 예외처리
if N == 1:
    print(int(ls[0]))
elif N == 3:
    print(cal(1, int(ls[0]), int(ls[2])))
#괄호 추가할 연산자 고르기
else:
    num = [i for i in range(1, N, 2)]
    comb = []
    for i in range(1, N // 4 + 1):
        comb.append(list(combinations(num, i)))
    comb = list(reduce(lambda x, y : x + y, comb))

    for i in range(len(comb) - 1, N // 2 - 1, -1):
        for j in range(len(comb[i]) - 1):
            if comb[i][j] + 2 == comb[i][j + 1]:
                comb.pop(i)
                break

    #연산하기
    m = -2147483648

    for i in range(len(comb)):
        result = int(ls[0])
        j = 2
        if 1 in comb[i]:
            result = cal(1, int(ls[0]), int(ls[2]))
            j = 4
            
        #print(j, result)
        while j < N:
            if j + 1 in comb[i]:
                result = cal(j - 1, result, cal(j + 1, int(ls[j]), int(ls[j + 2])))
                #print(j, result)
                j += 4
                
            else:
                result = cal(j - 1, result, int(ls[j]))
                #print(j, result)
                j += 2
        if result > m:
            m = result
    print(m)
