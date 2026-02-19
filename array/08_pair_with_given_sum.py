def find_pair_with_sum(arr, target):
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
    return None

if __name__ == '__main__':
    arr = [2, 7, 4, 0, 9, 5, 1, 3]
    target = 9
    print("Array:", arr)
    print("Target Sum:", target)
    pair = find_pair_with_sum(arr, target)
    if pair:
        print("Pair found:", pair[0], "+", pair[1], "=", target)
    else:
        print("No pair found")
