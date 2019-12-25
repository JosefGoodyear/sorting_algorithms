def merge(list1, list2):
    """ merge two lists together """
    index_1 = 0
    index_2 = 0
    merged_list = []
    while index_1 < len(list1) and index_2 < len(list2):
        if list1[index_1] < list2[index_2]:
            merged_list.append(list1[index_1])
            index_1 += 1
        else:
            merged_list.append(list2[index_2])
            index_2 += 1
    merged_list.extend(list1[index_1:])
    merged_list.extend(list2[index_2:])
    return merged_list

def merge_sort(arr):
    """ Time Complexity: O(nlogn)
        Space Complexity: n
        NOTE: Generally merge sort does not sort in place,
        as in this implementation.
    """
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    l1 = merge_sort(arr[0:mid])
    l2 = merge_sort(arr[mid:len(arr)])
    return merge(l1, l2)

l = [9, 2, 1, 4, 3, 2, 10, 6]

print(l)
sorted_list = merge_sort(l)
print(sorted_list)