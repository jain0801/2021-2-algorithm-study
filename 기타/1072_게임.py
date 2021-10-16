import math

x, y = map(int, input().split())
A = math.trunc(y / x * 100)
result = ((100 * y) - (A + 1) * x) / (A - 99)
check = 0
if result == math.trunc(result):
    check = 1
result = math.trunc(result)

if A >= 99:
    print(-1)
else:
    if check == 0:
        print(result + 1)
    else:
        print(result)
