def insertion_sort(arr):
    """ Time Complexity: O(n^2) - worst, average
                         O(n) - best
        Space Complexity: O(1)
    """
    for i in range(len(arr) - 1):
        while arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            if i > 0:
                i -= 1

li = [5, 4, 3, 2, 1]
insertion_sort(li)
print(li)