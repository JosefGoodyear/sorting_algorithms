def partition(arr, lo, hi):
    i = lo
    j = lo - 1
    for i in range(lo, hi):
        if arr[i] < arr[hi]:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[j + 1], arr[hi] = arr[hi], arr[j + 1]
    return j + 1

def quick_sort(arr, lo, hi):
    """ Time Complexity: Worst - O(n^2), Average - O(nlogn)
        Space Complexity: O(n)
    """
    if lo < hi:
        pivot = partition(arr, lo, hi)
        quick_sort(arr, lo, pivot - 1)
        quick_sort(arr, pivot + 1, hi)


li = [2, 5, 1, 0, 3, 8]

print(li)
quick_sort(li, 0, len(li) - 1)
print(li)