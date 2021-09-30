N, K = map(int, input().split())

value = [list(map(int, input().split())) for i in range(N)]
value.sort(key = lambda x : x[0])
bag = [0 for i in range(K + 1)]

for i in value:
    tmp = [i for i in bag]
    tmp[i[0]] = max(bag[i[0]], i[1])
    for j in range(1, K + 1):
        if j + i[0] > K:
            break
        tmp[j + i[0]] = max(bag[j + i[0]], bag[j] + i[1])
    bag = tmp

print(max(bag))
