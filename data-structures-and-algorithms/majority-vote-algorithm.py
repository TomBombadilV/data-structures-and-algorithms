# Majority Vote Algorithm
# https://www.cs.utexas.edu/~moore/best-ideas/mjrty/
# Time: O(n) | Space: O(1)

from typing import List

def get_majority(arr: List[int]) -> int:
    n, count = -1, 0
    for a in arr:
        if count == 0:
            n = a
            count += 1
        else:
            count = count + 1 if a == n else count - 1
    return n

print(get_majority([1, 2, 3, 1, 2, 2, 1, 1, 1]))
print(get_majority([1, 1, 1, 2, 2, 3, 3, 2, 2, 2, 3, 2, 2]))