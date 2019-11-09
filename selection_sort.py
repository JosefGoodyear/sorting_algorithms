def selection_sort(arr):
    """ Time Complexity: O(n^2) - worst, average
                         O(n) - best
        Space Complexity: O(1)
    """
    for i in range(len(arr)):
        min_pos = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_pos]:
                min_pos = j
        arr[min_pos], arr[i] = arr[i], arr[min_pos]

li = [5, 4, 3, 2, 1]
selection_sort(li)
print(li)