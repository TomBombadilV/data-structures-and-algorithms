from binarysearchtree import BSTNode, BinarySearchTree
from typing import Union

class AVLNode(BSTNode):
    def __init__(self, val: int):
        super().__init__(val)
        # Difference between left and right subtree heights
        # Height of right - height of left
        self.balance = 0

class AVLTree(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def insert(self, val: int) -> None:
        
        def insert_node(root: AVLNode, val: int) -> None:
            if val < root.val:
                if root.left:
                    insert_node(root.left, val)
                else:
                    root.left = AVLNode(val)
            elif val > root.val:
                if root.right:
                    insert_node(root.right, val)
                else:
                    root.right = AVLNode(val)
            else:
                return
      
        # I was going to update the balance inside the insert_node function.
        # The problem is if a duplicate is inserted into the tree, then we'd
        # have to go back and reverse all of the updated balances. Running it
        # as a separate function will add an additional logn traversal.
        def update_balance( root: AVLNode, 
                            val: int, 
                            rotation_type: str,
                            rotation_node: AVLNode) -> Union[str, AVLNode]:
            # If no root or value found, no more nodes to visit
            if not(root) or val == root.val:
                return rotation_type, rotation_node
            # If value is to the left of root
            if val < root.val:
                # Update balance to reflect increase in left subtree
                root.balance -= 1
                if len(rotation_type) == 1:
                    rotation_type += 'L'
                if not(rotation_type) and abs(root.balance) > 1:
                    rotation_type += 'L'
                    rotation_node = root
                return update_balance(root.left, val, rotation_type, rotation_node)
            # val > root.val
            else:
                root.balance += 1
                if len(rotation_type) == 1:
                    rotation_type += 'R'
                if not(rotation_type) and abs(root.balance) > 1:
                    rotation_type += 'R'
                    rotation_node = root
                return update_balance(root.right, val, rotation_type, rotation_node)

        def rotate_ll(root: AVLNode):
            if root == self.root:
                self.root = left
            else:
                parent = root.parent
                parent.??? = left
                left.parent = parent
            left = root.left
            left_left = left.left
            left_right = left.right
            left.parent = 
            left.right = root
            root.parent = left
            root.left = left_right
            left_right.parent = root

        def rotate_lr(root: AVLNode):
            pass

        def rotate_rr(root: AVLNode):
            pass

        def rotate_rl(root: AVLNode):
            pass

        if not(self.root):
            self.root = AVLNode(val)
        else:
            insert_node(self.root, val)
            rotation_type, rotation_node = update_balance(self.root, val, '', None)
            if rotation_type:
                print(rotation_type, rotation_node.val)

def test_avl_tree():
    l = [1, 2, 3, 4]
    avl = AVLTree()
    for n in l:
        avl.insert(n)
        avl.print_tree()

if __name__ == '__main__':
    test_avl_tree()
