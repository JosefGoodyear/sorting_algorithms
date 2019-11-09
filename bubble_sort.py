def bubble_sort(arr):
    """ Time Complexity: O(n^2) - worst, average
                         O(n) - best
        Space Complexity: O(1)
    """
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

li = []
bubble_sort(li)
print(li)