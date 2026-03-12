from collections import defaultdict
t = int(input("Enter number of test cases: "))
for i in range(t):
    n = int(input("Enter number of dishes: "))
    arr = list(map(int, input("Enter dish types: ").split()))
    pos = defaultdict(list)
    for i in range(n):
        pos[arr[i]].append(i)
    best_count = 0
    best_type = float('inf')
    for dish in pos:
        last = -2
        count = 0
        for p in pos[dish]:
            if p - last > 1: 
                count += 1
                last = p
        if count > best_count or (count == best_count and dish < best_type):
            best_count = count
            best_type = dish
    print("Best dish type:", best_type)
    