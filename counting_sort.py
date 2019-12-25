def counting_sort(nums, max_val):
    """ NOTE: counting sort requires all values to be positive 
        Time Complexity: O(n + k), where n is nums and k is range of max_val
    """ 
    count_array = [0] * (max_val + 1)
    sorted_array = []
    for num in nums:
        count_array[num] += 1
    for value, count in enumerate(count_array):
        while count > 0:
            sorted_array.append(value)
            count -= 1
    return sorted_array
arr = [8, 100, 5, 11, 13, 12, 97, 98, 32, 32, 33]

print(counting_sort(arr, 100))
