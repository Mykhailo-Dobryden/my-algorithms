def binary_search(lists, item):
    low = 0
    high = len(lists) - 1

    while low <= high:
        mid = (low + high)
        guess = lists[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = list(range(1, 100, 2))
print(my_list)

print(binary_search(my_list, 55))
