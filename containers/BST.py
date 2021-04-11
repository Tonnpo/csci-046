from containers.BinaryTree import BinaryTree, Node


class BST(BinaryTree):

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the BST.
        '''
        super().__init__()
        if xs is not None:
            self.insert_list(xs)

    def __repr__(self):
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_bst_satisfied(self):
        if self.root:
            return BST._is_bst_satisfied(self.root)
        return True

    @staticmethod
    def _is_bst_satisfied(node):
        ret = True
        if node.left:
            if node.value >= BST._find_largest(node.left):
                ret &= BST._is_bst_satisfied(node.left)
            else:
                ret = False
        if node.right:
            if node.value <= BST._find_smallest(node.right):
                ret &= BST._is_bst_satisfied(node.right)
            else:
                ret = False
        return ret

    def insert(self, value):
        if self.root:
            BST._insert(value, self.root)
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(value, node):
        if value > node.value:
            if node.right:
                BST._insert(value, node.right)
            else:
                node.right = Node(value)
        elif value < node.value:
            if node.left:
                BST._insert(value, node.left)
            else:
                node.left = Node(value)
        else:
            pass

    def insert_list(self, xs):
        for x in xs:
            self.insert(x)

    def __contains__(self, value):
        '''
        Recall that `x in tree` desugars to `tree.__contains__(x)`.
        '''
        return self.find(value)

    def find(self, value):
        '''
        Returns whether value is contained in the BST.

        FIXME:
        Implement this function.
        '''
        if self.root is None:
            return False
        else:
            return BST._find(value, self.root)

    @staticmethod
    def _find(value, node):
        '''
        FIXME:
        Implement this function.
        '''
        ret = True
        if node is not None:
            if value > node.value:
                if node.right is not None:
                    ret &= BST._find(value, node.right)
                else:
                    ret = False
            elif value < node.value:
                if node.left is not None:
                    ret &= BST._find(value, node.left)
                else:
                    ret = False
            else:
                ret &= (value == node.value)
            return ret
        else:
            return False

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.
        '''
        if self.root is None:
            raise ValueError('Nothing in tree')
        else:
            return BST._find_smallest(self.root)

    @staticmethod
    def _find_smallest(node):
        assert node is not None
        if node.left is None:
            return node.value
        else:
            return BST._find_smallest(node.left)

    def find_largest(self):
        '''
        Returns the largest value in the tree.

        FIXME:
        Implement this function.

        HINT:
        Follow the pattern of the _find_smallest function.
        '''
        if self.root is None:
            raise ValueError('Nothing in tree')
        else:
            return BST._find_largest(self.root)

    def _find_largest(node):
        assert node is not None
        if node.right is None:
            return node.value
        else:
            return BST._find_largest(node.right)

    def remove(self, value):
        if self.root is not None:
            if self.root.value == value and self.__len__() == 1:
                self.root = None
            else:
                BST._remove(value, self.root)

    @staticmethod
    def _remove(value, node):
        parent = None
        while node and node.value != value:
            parent = node
            if value > node.value:
                node = node.right
            elif value < node.value:
                node = node.left
        if node:
            if node.left is None and node.right is None:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
            else:
                if node.left is not None and node.right is None:
                    temp = node.left
                    node.value = temp.value
                    node.left = temp.left
                    node.right = temp.right
                elif node.right is not None and node.left is None:
                    temp = node.right
                    node.value = temp.value
                    node.left = temp.left
                    node.right = temp.right
                else:
                    temp = BST._find_largest(node.left)
                    BST._remove(temp, node)
                    node.value = temp

    def remove_list(self, xs):
        '''
        Given a list xs, remove each element of xs from self.

        FIXME:
        Implement this function.

        HINT:
        See the insert_list function.
        '''
        for x in xs:
            self.remove(x)
