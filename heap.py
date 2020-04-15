from random import shuffle

class Heap:
    def __init__(self):
        self.arr = []

    # Insert a node into heap
    def put(self, n: int) -> None:
        # Insert into bottommost, rightmost position
        self.arr.append(n)
        # Bubble up if necessary
        i = len(self.arr) - 1
        # Use ceiling division to find parent index
        parent_i = -(-i // 2) - 1
        while parent_i >= 0 and self.arr[parent_i] > self.arr[i]:
            # Swappy swap if parent is larger than child
            self.arr[parent_i], self.arr[i] = self.arr[i], self.arr[parent_i]
            # Check new parent using ceiling division
            i, parent_i = parent_i, -(-parent_i // 2) - 1

    # Returns index of child with smaller value
    def smaller_child_index(self, parent_i: int) -> int:
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

    # Gets min from heap
    def get(self) -> int:
        # Save the original min value (root)
        res = self.arr[0]
        # Place the last element into the root
        self.arr = self.arr[1:]
        self.arr = self.arr[-1:] + self.arr[:-1]
        parent_i = 0
        child_i = self.smaller_child_index(parent_i)
        # If no children, nothing more to do
        if child_i == -1: 
            return res
        # Keep swapping as long as parent is larger than child and child is valid
        while not(child_i == -1) and self.arr[parent_i] > self.arr[child_i]:
            self.arr[parent_i], self.arr[child_i] = self.arr[child_i],\
                                                    self.arr[parent_i]
            parent_i = child_i
            child_i = self.smaller_child_index(parent_i)
        return res
    
    # Makes sure that heap invariant is held (every parent is >= its children)
    def verify(self) -> None:
        # Iterate through array excluding root node
        for i in range(1, len(self.arr)):
            # Check if parent is larger than child
            parent_i = -(-i // 2) - 1
            if self.arr[parent_i] > self.arr[i]:
                print(  "Heap violation: {0} is a parent of {1} at indices {2}"
                        "and {3}.".format(  self.arr[parent_i], 
                                            self.arr[i], 
                                            parent_i, i))
                return
        print("Heap verified.")

    # Prints heap in layers
    def print_heap(self) -> None:
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

#l = [i for i in range(15)]
#shuffle(l)
l = [5, 8, 1, 9, 4, 14, 6, 11, 12, 0, 7, 13, 3, 2, 10]
sorted_l = []
print(l)
h = Heap()
for n in l:
    h.put(n)
h.print_heap()
for _ in range(len(l)):
    sorted_l.append(h.get())
    h.verify()
print(sorted_l)
h.print_heap()
