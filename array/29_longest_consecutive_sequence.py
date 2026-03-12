def longest_consecutive_sequence(arr):
    if not arr:
        return 0
    num_set = set(arr)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            longest = max(longest, current_streak)
    return longest

if __name__ == '__main__':
    arr = [100,  200, 1, 3, 2]
    print("Array:", arr)
    print("Longest Consecutive Sequence Length:", longest_consecutive_sequence(arr))
