from random import shuffle

class BSTNode:
    def __init__(self, val: int):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        self.type = None

class BinarySearchTree:
    def __init__(self):
         self.root = None
    
    def insert(self, val:int) -> None:
        if not(self.root):
            self.root = BSTNode(val)
            return
        curr = self.root
        while curr:
            if val < curr.val:
                if not(curr.left):
                    curr.left = BSTNode(val)
                    curr.left.parent = curr
                    curr.left.type = 0
                    return
                else:
                    curr = curr.left
            elif val > curr.val:
                if not(curr.right):
                    curr.right = BSTNode(val)
                    curr.right.parent = curr
                    curr.right.type = 1
                    return
                else:
                    curr = curr.right
            # No duplicates plz 
            else:
                return
    
    def find(self, val: int) -> BSTNode:
        curr = self.root
        while curr:
            if curr.val == val:
                return curr
            elif curr.val > val:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def update_parents_child(self, old_child: BSTNode, new_child: BSTNode) -> None:
        # Get parent
        parent = old_child.parent
        # If node was a left child
        if old_child.type == 0:
            parent.left = new_child
        # If node was a right child
        else:
            parent.right = new_child

    # Return max value of tree starting at given node. Default is root
    def get_max(self, root: BSTNode = None) -> BSTNode:
        def get_max_util(root: BSTNode, max_node: BSTNode) -> BSTNode:
            if root:
                # Get max of left subtree
                left_max = get_max_util(root.left, max_node)
                # Get max of right subtree
                right_max = get_max_util(root.right, max_node)
                # Check root, left max and right max for max
                if root.val > max_node.val:
                    max_node = root
                if left_max.val > max_node.val:
                    max_node = left_max
                if right_max.val > max_node.val:
                    max_node = right_max
            return max_node

        # If no root node given, set to root
        if root == None:
            root = self.root
        return get_max_util(root, root)

    def delete(self, val) -> None:
        # Find the corresponding node
        node = self.find(val)
        # Node doesn't exist in tree
        if not(node):
            print("Node does not exist in the tree.")
            return
        # Node is root
        if node == self.root:
            self.root = None
            return
        # Node has no children (yey :D)
        if not(node.left) and not(node.right):
            self.update_parents_child(node, None)
        # Node has only left child
        elif not(node.right):
            self.update_parents_child(node, node.left)
        # Node has only right child
        elif not(node.left):
            self.update_parents_child(node, node.right)
        # Node has both children D:
        else:
            # Get max of left subtree (natural predecessor)
            max_left_subtree = get_max(node.left)
            # Swap value of node with value of max of left subtree
            max_left_subtree.val, node.val = node.val, max_left_subtree.val
            # Delete node of left subtree max (deletes node value)
            self.delete(max_left_subtree)
            # 

    def depth(self) -> int:
        def max_depth_util(node: BSTNode) -> int:
            if not(node):
                return 0
            return 1 + max(max_depth_util(node.left), max_depth_util(node.right))
        
        return max_depth_util(self.root)

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
print("Tree max: ", rbst.get_max(rbst.root).val)
