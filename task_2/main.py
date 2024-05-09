"""This module implements Binary search function for float numbers"""


def binary_search(arr, x):
    """Binary search function"""
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0

    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            result = (iterations, arr[mid])
            print(result)
            return

    if arr[mid] < x:
        result = (iterations, arr[mid + 1] if mid + 1 < len(arr) else None)
        print(result)
        return
    else:
        result = (iterations, arr[mid])
        print(result)
        return


# test cases
numbers = [2.3, 5.7, 13.2, 19.25]
number = 9.2

binary_search(numbers, number)
