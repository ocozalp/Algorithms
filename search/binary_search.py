def binary_search(array, target_value):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) / 2
        if array[mid] == target_value:
            return mid

        if array[mid] > target_value:
            right = mid - 1
        elif array[mid] < target_value:
            left = mid + 1

    return right + 1