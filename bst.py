from random import shuffle

class BSTNode:
    def __init__(self, val: int):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        # Whether node is a right (1) or left (0) child
        self.type = -1

class BinarySearchTree:
    def __init__(self):
         self.root = None
    
    # Inserts a node with the given value
    def insert(self, val:int) -> None:
        # If no root, set as new root
        if not(self.root):
            self.root = BSTNode(val)
            return
        curr = self.root
        while curr:
            if val < curr.val:
                if not(curr.left):
                    # Add to tree as left child
                    curr.left = BSTNode(val)
                    curr.left.parent = curr
                    curr.left.type = 0
                    return
                else:
                    curr = curr.left
            elif val > curr.val:
                if not(curr.right):
                    # Add to tree as right child
                    curr.right = BSTNode(val)
                    curr.right.parent = curr
                    curr.right.type = 1
                    return
                else:
                    curr = curr.right
            # If value already exists in tree, then stop 
            else:
                print("Node already exists in tree.")
                return
   
    # Returns node with corresponding value
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

    # Delete node with given value. Also have option of passing in a node.
    def delete(self, val: int, override: BSTNode = None) -> None:
        
        # Changes parent's child to new node
        def update_parents_child(old_child: BSTNode, new_child: BSTNode) -> None:
            # Get parent
            parent = old_child.parent
            # No parent means node is root node
            if not(parent):
                self.root = new_child
            # If node was a left child
            elif old_child.type == 0:
                parent.left = new_child
            # If node was a right child
            else:
                parent.right = new_child

        # Swaps node value with value of max of left subtree and deletes old node
        def swap_and_delete(node: BSTNode) -> None:
            # Get max of left subtree (natural predecessor)
            max_left_subtree = self.get_max(node.left)
            # Swap value of node with value of max of left subtree
            max_left_subtree.val, node.val = node.val, max_left_subtree.val
            # Delete node of left subtree max (deletes node value)
            self.delete(None, max_left_subtree)

        # Checks which deletion case to use and performs deletion
        def perform_delete(node: BSTNode) -> None:
             # Node has no children (yey :D)
            if not(node.left) and not(node.right):
                # Set parent to point to None
                update_parents_child(node, None)
            # Node has only left child
            elif not(node.right):
                # Set parent to point to node's left child
                update_parents_child(node, node.left)
            # Node has only right child
            elif not(node.left):    
                # Set parent to point to node's right child
                update_parents_child(node, node.right)
            # Node has both children D:
            else:
                # Swap with and delete node max of left subtree
                swap_and_delete(node)
        
        # If no node passed, in look up by value
        if not(override):
            # Find the corresponding node
            node = self.find(val)
            # Node doesn't exist in tree
            if not(node):
                print("Node doesn't exist in tree.")
                return
        # Node passed in
        else:
            node = override
        # Delete the node
        print("Deleting node ", node.val)
        perform_delete(node)
       
    # Returns maximum depth of tree
    def depth(self) -> int:
        def max_depth_util(node: BSTNode) -> int:
            if not(node):
                return 0
            return 1 + max(max_depth_util(node.left), max_depth_util(node.right))
        
        return max_depth_util(self.root)

    # Prints entire tree
    def print_tree(self) -> None:
        def print_tree_util(node: BSTNode, branch: str, child_branch: str) -> None:
            print(branch, node.val)
            if node.left and node.right:
                print_tree_util(node.left, child_branch + '├───', child_branch + '│    ')
            if node.left and not(node.right):
                print_tree_util(node.left, child_branch + '└───', child_branch + '     ')
            if node.right:
                print_tree_util(node.right, child_branch + '└───', child_branch + '     ')
        print_tree_util(self.root, '', '')

class RandomBST(BinarySearchTree):
    def __init__(self, n: int):
        super().__init__()
        l = [i for i in range(n)]
        shuffle(l)
        print(l)
        for i in l:
            self.insert(i)

rbst = RandomBST(10)
rbst.print_tree()
print("Tree max: ", rbst.get_max(rbst.root).val)
print("Deleting node 0")
rbst.delete(0)
rbst.print_tree()
