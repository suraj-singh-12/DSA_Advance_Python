def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    unique_vals = set(arr)
    answer = -1
    best = 0
    for val in unique_vals:
        idx = []
        for i, x in enumerate(arr):
            if x == val:
                idx.append(i)
        cnt = 0
        last = -2
        for i in idx:
            if i != last + 1:
                cnt += 1
            last = i
        if cnt > best:
            best = cnt
            answer = val
        elif cnt == best:
            answer = min(answer, val)
    print(answer)
t = int(input())
for i in range(t):
    solve()