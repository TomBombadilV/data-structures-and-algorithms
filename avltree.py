from binarysearchtree import BSTNode, BinarySearchTree

class AVLNode(BSTNode):
    def __init__(self, val: int):
        super().init__(val)
        # Difference between left and right subtree heights
        # Height of right - height of left
        self.balance = 0

class AVLTree(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def insert(self, val: int) -> None:
        def recurse(root: AVLNode, val: int):
            if not(self.root):
                self.root = AVLNode(val)
            if val < root.val:
                root.balance -= 1
                if root.left:
                    recurse(root.left, val)
                else:
                    root.left = AVLNode(val)
            elif val > root.val:
                root.balance += 1
                if root.right:
                    recurse(root.right, val)
                else:
                    root.right = AVLNode(val)
            else:
                return

def test_avl_tree():
    l = [1, 2, 3, 4]
    avl = AVLTree()
    for n in l:
        avl.insert(n)
        avl.print_tree()

if __name__ == '__main__':
    test_avl_tree()
