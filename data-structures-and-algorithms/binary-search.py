# Binary Search

from typing import List

def binary_search_recursive(l: List, n: int):
    if len(l) == 0:
        return False
    mid = len(l) // 2
    if n == l[mid]:
        return True
    if n < l[mid]:
        return binary_search_recursive(l[:mid], n)
    if n > l[mid]:
        return binary_search_recursive(l[mid+1:], n)

def binary_search_iterative(l: List, n: int):
    left, right =  0, len(l) - 1
    while left <= right:
        mid = (right + left) // 2
        if l[mid] == n:
            return True
        elif n < l[mid]:
            right = mid - 1
        # n > l[mid]
        else:
            left = mid + 1
    return False
    
    
l = [1, 2, 3, 6, 8, 11, 15, 26, 45]
print(binary_search_recursive(l, 6))
print(binary_search_recursive(l, 7))
print(binary_search_recursive(l, 45))
print(binary_search_iterative(l, 6))
print(binary_search_iterative(l, 7))
print(binary_search_iterative(l, 45))