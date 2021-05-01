class Node():

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left    # NOTE: left should always be a Node
        self.right = right  # NOTE: right should always be a Node

    def __str__(self):
        ret = '('
        ret += str(self.value)
        ret += ' - '
        if self.left:
            ret += str(self.left)
            ret += ' '
        ret += '- '
        if self.right:
            ret += str(self.right)
            ret += ' '
        ret += ')'
        return ret


class BinaryTree():
    '''
    This class is relatively useless by itself,
    but it is the superclass for the BST, AVLTree, and Heap classes,
    and it provides important helper functions for these classes.
    If you don't implement all of the functions in this class correctly,
    it will be impossible to implement those other classes.
    '''

    def __init__(self, root=None):
        if root:
            self.root = Node(root)
        else:
            self.root = None

    def __str__(self):
        '''
        We can visualize a tree by visualizing its root node.
        '''
        return str(self.root)

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_print(self.root, '')
        elif traversal_type == 'inorder':
            return self.inorder_print(self.root, '')
        elif traversal_type == 'postorder':
            return self.postorder_print(self.root, '')
        else:
            raise ValueError('Traversal type is not supported.')

    def preorder_print(self, start, traversal):
        '''
        Prints the nodes using a preorder traversal.
        '''
        if start:
            traversal += str(start.value) + '-'
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        '''
        Prints the nodes using a inorder traversal.
        '''
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += str(start.value) + '-'
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        '''
        Prints the nodes using a postorder traversal.
        '''
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += str(start.value) + '-'
        return traversal

    def to_list(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder(self.root, traversal_type)
        elif traversal_type == 'inorder':
            return self.inorder(self.root, traversal_type)
        elif traversal_type == 'postorder':
            return self.postorder(self.root, traversal_type)
        else:
            raise ValueError('Traversal type is not supported.')

    def preorder(self, start, traversal):
        '''
        FIXME:
        Implement this function by modifying the _print functions above.
        '''
        res = []
        if start:
            res.append(start.value)
            res += self.preorder(start.left, traversal)
            res += self.preorder(start.right, traversal)
        return res

    def inorder(self, start, traversal):
        '''
        FIXME:
        Implement this function by modifying the _print functions above.
        '''
        res = []
        if start:
            res += self.inorder(start.left, traversal)
            res.append(start.value)
            res += self.inorder(start.right, traversal)
        return res

    def postorder(self, start, traversal):
        '''
        FIXME:
        Implement this function by modifying the _print functions above.
        '''
        res = []
        if start:
            res += self.postorder(start.left, traversal)
            res += self.postorder(start.right, traversal)
            res.append(start.value)
        return res

    def __len__(self):
        '''
        Returns the number of elements contained in the tree.
        Recall that `tree.__len__()` will desugar to `size(len)`.
        '''
        return BinaryTree.__len__helper(self.root)

    @staticmethod
    def __len__helper(node):
        '''
        FIXME:
        Implement this function.

        HINT:
        The pseudocode is:
        add 1 for the current node;
        return the sum of these three steps
        '''
        res = 0
        if node:
            res += 1
            if node.left:
                res += BinaryTree.__len__helper(node.left)
            if node.right:
                res += BinaryTree.__len__helper(node.right)
        return res

    def height(self):
        '''
        Returns the height of the tree.

        FIXME:
        Implement this function.

        HINT:
        See how the __len__ method calls its helper staticmethod.
        '''
        return BinaryTree._height(self.root)

    @staticmethod
    def _height(node):
        '''
        FIXME:
        Implement this function.

        HINT:
        The pseudocode is:
        if a left child exists, calculate the _height of the left child;
        if a right child exists, calculate the _height of the right child;
        '''
        left_height = 0
        right_height = 0
        if node:
            left_height = BinaryTree._height(node.left) if node.left else -1
            right_height = BinaryTree._height(node.right) if node.right else -1
            return 1 + max(left_height, right_height)
        else:
            return -1
