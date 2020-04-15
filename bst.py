from random import Shuffle

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

class RandomBST(BinarySearchTree):
    def __init__(self, n: int):
        l = [i for i in range(n)]




bst = BinarySearchTree()

