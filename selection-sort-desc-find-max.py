def find_max(arr):
    maximal = arr[0]
    maximal_index = 0
    for i in range(1, len(arr)):
        if arr[i] > maximal:
            maximal = arr[i]
            maximal_index = i
    return maximal_index


def selection_sort_desc(arr):
    new_arr = []
    for i in range(len(arr)):
        maximal_item = find_max(arr)
        new_arr.append(arr.pop(maximal_item))
    return new_arr


arr_test = [54, 23, 90, 12, 86, 62, 64, 9, 10, 11]

print(find_max(arr_test))
print(selection_sort_desc(arr_test))
