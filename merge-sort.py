# Merge Sort
# Time: nlogn | Space: O(n)

from typing import List

def merge(nums: List[int]) -> List[int]:
    if len(nums) == 1:
        return nums
    # Do merge sort on the two halves of the given array
    mid = len(nums) // 2
    arr_a, arr_b = merge(nums[:mid]), merge(nums[mid:])
    # Merge the two halves together in sorted order
    ans = []
    while arr_a and arr_b:
        if arr_a[0] < arr_b[0]:
            ans.append(arr_a[0])
            arr_a = arr_a[1:]
        else:
            ans.append(arr_b[0])
            arr_b = arr_b[1:]
    # If one array was longer than the other, add remaining elemnts
    if arr_a:
        ans = ans + arr_a
    elif arr_b:
        ans = ans + arr_b
    return ans

print(merge([12, 11, 13, 5, 6, 7]))