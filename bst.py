from random import shuffle

class BSTNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
         self.root = None
    
    def insert(self, val) -> None:
        if not(self.root):
            self.root = BSTNode(val)
            return
        curr = self.root
        while curr:
            if val < curr.val:
                if not(curr.left):
                    curr.left = BSTNode(val)
                    return
                else:
                    curr = curr.left
            elif val > curr.val:
                if not(curr.right):
                    curr.right = BSTNode(val)
                    return
                else:
                    curr = curr.right
            # No duplicates plz 
            else:
                return
    
    def diameter(self) -> int:
        def diameter_left(node: BSTNode, left_width: int) -> int:
            if not(node):
                return 0
            left_width += max(  diameter_left(node.left, 1), \
                                diameter_left(node.right, -1))
            return left_width
            
        def diameter_right(node: BSTNode, right_width: int) -> int:
            if not(node):
                return 0
            right_width += max( diameter_right(node.left, -1), \
                                diameter_right(node.right, 1))
            return right_width

        if not(self.root): return 0
        return 1 \
               + diameter_left(self.root.left, 1)\
               + diameter_right(self.root.right, 1)

    def print_tree(self) -> None:
        q = []
        curr = self.root
        level = 0
        while curr or q:
            print(curr.val, end=" ")
            if curr.left:
                q.append((curr.left, level + 1))
            if curr.right:
                q.append((curr.right, level + 1))
            prev_level = level
            curr, level = q[0] if q else (None, None)
            if not(level == prev_level):
                print()
            q = q[1:]


class RandomBST(BinarySearchTree):
    def __init__(self, n: int):
        super().__init__()
        l = [i for i in range(n)]
        shuffle(l)
        for i in l:
            self.insert(i)

rbst = RandomBST(10)
rbst.print_tree()
print("Width: ", rbst.diameter())
