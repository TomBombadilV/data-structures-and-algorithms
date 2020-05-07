from random import shuffle

from typing import Tuple, Union

class Heap:
    """
    Implementation of heap that supports:
    - insert (of ints, strings, and tuples)
    - delete
    - get
    - verify
    - print
    """
    def __init__(self):
        self.arr = []
        self.indices = {}  # Preserve indices for constant time lookup
   
    def _swap(self, i: int, j: int) -> None:
        """
        Swaps elements in given indices
        """
        # Swappy swap
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        
        # Update indices
        self.indices[self.arr[i]] = i
        self.indices[self.arr[j]] = j

    def put(self, n: Union[int, str, Tuple]) -> None:
        """
        Inserts a node into the heap
        """
        # Insert into bottommost, rightmost position
        self.arr.append(n)
        self.indices[n] = len(self.arr) - 1  # Save index

        # Use ceiling division to find parent index
        i = len(self.arr) - 1
        parent_i = -(-i // 2) - 1
        
        # Bubble up if necessary
        while parent_i >= 0 and self.arr[parent_i] > self.arr[i]:
            # Swappy swap
            self._swap(parent_i, i)
            # Check new parent using ceiling division
            i, parent_i = parent_i, -(-parent_i // 2) - 1

    def _smaller_child_index(self, parent_i: int) -> int:
        """
        Returns the index of the child with smaller value
        """
        # Check if parent index is valid
        if parent_i < 0 or parent_i >= len(self.arr):
            return -1
        
        # Calculate indices of left and right children
        child_l = parent_i * 2 + 1
        child_r = parent_i * 2 + 2
        
        # If left child is out of range of array, parent has no children 
        # (because this is a perfectly balanced tree)
        if child_l >= len(self.arr):
            return -1
        
        # If right child is out of range of array OR left child is smaller than 
        # right child, return index of left child
        if  child_r >= len(self.arr) or \
            self.arr[child_l] <= self.arr[child_r]:
            return child_l
        
        # If both children exist and right child is greater than left child, 
        # return right child
        return child_r

    def get(self) -> int:
        """
        Deletes and returns min and re-heapifies
        """ 
        # Save the original min value (root)
        res = self.arr[0]
        
        # Delete min
        self.arr = self.arr[1:]
        del self.indices[res]

        # Place the last element into the root
        self.arr = self.arr[-1:] + self.arr[:-1]
        self.indices[self.arr[0]] = 0

        # Calculate parent and child indices
        parent_i = 0
        child_i = self._smaller_child_index(parent_i)
        
        # If no children, nothing more to do
        if child_i == -1: 
            return res
        
        # Keep swapping as long as parent is larger than child and child is valid
        while not(child_i == -1) and self.arr[parent_i] > self.arr[child_i]:
            # Swappy swap
            self._swap(parent_i, child_i)
            
            # Calculate new indices
            parent_i = child_i
            child_i = self._smaller_child_index(parent_i)
        return res
   
    def delete(self, val: Union[int, str, Tuple]) -> None:
        # Make sure value exists in heap
        if not(val in self.indices):
            print("Value does not exist in heap.")
            return

        i = self.indices[val]
        del self.indices[val]
        
        # Place the last element into deleted index
        self.arr[i] = self.arr[-1]
        self.arr = self.arr[:-1]

        # Calculate parent and child indices
        parent_i = i
        child_i = self._smaller_child_index(parent_i)
        
        # If no children, nothing more to do
        if child_i == -1: 
            return 
        
        # Keep swapping as long as parent is larger than child and child is valid
        while not(child_i == -1) and self.arr[parent_i] > self.arr[child_i]:
            # Swappy swap
            self._swap(parent_i, child_i)
            
            # Calculate new indices
            parent_i = child_i
            child_i = self._smaller_child_index(parent_i)

    def verify(self) -> None:
        """
        Makes sure that heap invariant is held (every parent is >= its children)
        """
        # Iterate through array excluding root node
        for i in range(1, len(self.arr)):
            # Check if parent is larger than child
            parent_i = -(-i // 2) - 1
            if self.arr[parent_i] > self.arr[i]:
                print(  "Heap violation: {0} is a parent of {1} at indices {2} "
                        "and {3}.".format(  self.arr[parent_i], 
                                            self.arr[i], 
                                            parent_i, i))
                return
        print("Heap verified.")

    def print_heap(self) -> None:
        """
        Prints heap in layers
        """ 
        # Keep track of how many nodes have been added to layer. Binary tree so
        # number of nodes in layer doubles each time
        count, size = 0, 1
        for i in range(len(self.arr)):
            print(self.arr[i], end=" ")
            count += 1
            # If limit reached, we filled a level
            if count == size:
                print()
                # Reset count, double level size
                count, size = 0, size * 2
        print()

if __name__ == '__main__':
    # Driver code
    n = 10
    l = [i for i in range(n)]
    
    # Randomize list of integers
    shuffle(l)
    sorted_l = []
    
     # Use heap to sort numbers in O(nlogn time) ^_^
    h = Heap()
    for i in l:
        h.put(i)
    h.print_heap()
    for _ in range(len(l)):
        sorted_l.append(h.get())
        h.verify()
    print(sorted_l)
    h.print_heap()

    # Test with tuples and deletion
    h = Heap()
    for i in l:
        h.put((i, str(i)))
    h.verify()
    h.print_heap()
    h.delete((0, '0'))
    h.print_heap()
    h.verify()
