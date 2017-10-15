"""
    Count the number of occurrences of a specific target given a sorted array.
    Trivial Way: O(n)
    Optimal Way: O(log(n)) (Binary Search)
    Goal: Find first occurrence of number, find last occurrence of number (Binary Search x2)
    Subtract 2 indices + 1 to get the distance between the two points of indices
"""


def num_occurrences(arr, target):

    if not arr:
        return -1

    first_occurrence = find_first(arr, target, 0, len(arr) - 1)
    if first_occurrence == -1:
        return first_occurrence

    second_occurrence = find_second(arr, target, first_occurrence, len(arr) - 1)
    if second_occurrence == -1:
        return second_occurrence

    return second_occurrence - first_occurrence + 1


def find_first(arr, target, left, right):

    if right >= left:
        middle = int((left + right) / 2)
        if middle == 0 or arr[middle-1] < target == arr[middle]:
            return middle
        elif arr[middle] < target:
            return find_first(arr, target, middle + 1, right)
        else:
            return find_first(arr, target, left, middle - 1)
    return -1


def find_second(arr, target, left, right):

    if right >= left:
        middle = int((left + right) / 2)
        if middle == len(arr) - 1 or arr[middle + 1] > target == arr[middle]:
            return middle
        elif arr[middle] > target:
            return find_second(arr, target, left, middle - 1)
        else:
            return find_second(arr, target, middle + 1, right)
    return -1


def main():

    empty_arr = []
    even_arr = [-10, -8, -8, 3, 2, 5, 5, 5, 7, 11, 11, 12]
    odd_arr = [-8, -8, 3, 1, 2, 4, 5]
    target = 5

    res1 = num_occurrences(empty_arr, target)
    print('Expected: -1', ' Actual: ', res1)
    res2 = num_occurrences(even_arr, target)
    print('Expected: 3', ' Actual: ', res2)
    res3 = num_occurrences(odd_arr, target)
    print('Expected: 1', ' Actual: ', res3)


if __name__ == '__main__':
    main()
