from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST
from copy import copy


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        ret = True
        if node:
            if abs(AVLTree._balance_factor(node)) <= 1:
                ret &= AVLTree._is_avl_satisfied(node.left)
                ret &= AVLTree._is_avl_satisfied(node.right)
            else:
                ret = False
        return ret

    @staticmethod
    def _left_rotate(node):
        if node.right:
            new_node = copy(node.right)
            left_child = new_node.left
            new_node.left = copy(node)
            new_node.left.right = left_child
            return new_node
        else:
            return node

    @staticmethod
    def _right_rotate(node):
        if node.left:
            new_node = copy(node.left)
            right_child = new_node.right
            new_node.right = copy(node)
            new_node.right.left = right_child
            return new_node
        else:
            return node

    def insert(self, value):
        if self.root:
            BST._insert(value, self.root)
            if not self.is_avl_satisfied():
                AVLTree._fix_balance(value, self.root)
        else:
            self.root = Node(value)

    @staticmethod
    def _fix_balance(value, node):
        if node:
            balanced = AVLTree._rebalance(node)
            node.value = balanced.value
            node.left = balanced.left
            node.right = balanced.right
            AVLTree._fix_balance(value, node.right)
            AVLTree._fix_balance(value, node.left)

    @staticmethod
    def _insert(value, node):
        if value > node.value:
            balanced_node = AVLTree._rebalance(node)
            node.value = balanced_node.value
            node.left = balanced_node.left
            node.right = balanced_node.right
            if node.right:
                AVLTree._insert(value, node.right)
            else:
                node.right = Node(value)
        elif value < node.value:
            balanced_node = AVLTree._rebalance(node)
            node.value = balanced_node.value
            node.left = balanced_node.left
            node.right = balanced_node.right
            if node.left:
                AVLTree._insert(value, node.left)
            else:
                node.left = Node(value)

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        new_balance = copy(node)
        if AVLTree._balance_factor(node) < -1:
            if AVLTree._balance_factor(node.right) > 0:
                new_balance.right = AVLTree._right_rotate(node.right)
                new_balance = AVLTree._left_rotate(new_balance)
            else:
                new_balance = AVLTree._left_rotate(node)
        elif AVLTree._balance_factor(node) > 1:
            if AVLTree._balance_factor(node.left) < 0:
                new_balance.left = AVLTree._left_rotate(node.left)
                new_balance = AVLTree._right_rotate(new_balance)
            else:
                new_balance = AVLTree._right_rotate(node)
        return new_balance
