from containers.BinaryTree import BinaryTree, Node


class Heap(BinaryTree):
    '''
    Heap is currently not a subclass of BinaryTree.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the Heap.
        '''
        super().__init__()
        self.size = 0
        if xs is not None:
            self.insert_list(xs)

    def __repr__(self):
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_heap_satisfied(self):
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        ret = True
        if node.left:
            if node.value > node.left.value:
                ret = False
            else:
                ret &= Heap._is_heap_satisfied(node.left)
        if node.right:
            if node.value > node.right.value:
                ret = False
            else:
                ret &= Heap._is_heap_satisfied(node.right)
        return ret

    def insert(self, value):
        '''
        Inserts value into the heap.
        '''
        self.size += 1
        if self.root:
            pos_bin = '{0:b}'.format(self.size)[1:]
            Heap._insert(value, pos_bin, self.root)
            if not self.is_heap_satisfied():
                while not self.is_heap_satisfied() and pos_bin:
                    Heap._fix_heap(pos_bin, pos_bin[-1], self.root)
                    pos_bin = pos_bin[:-1]
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(value, pos_bin, node):
        if pos_bin:
            if pos_bin[0] == '0':
                if node.left:
                    Heap._insert(value, pos_bin[1:], node.left)
                else:
                    node.left = Node(value)
            else:
                if node.right:
                    Heap._insert(value, pos_bin[1:], node.right)
                else:
                    node.right = Node(value)

    @staticmethod
    def _fix_heap(pos_bin, child_pos, node):
        parent_bin = pos_bin[:-1]
        while parent_bin:
            if parent_bin[0] == '0':
                node = node.left
                parent_bin = parent_bin[1:]
            else:
                node = node.right
                parent_bin = parent_bin[1:]
        if child_pos == '0':
            if node.value > node.left.value:
                temp = node.value
                node.value = node.left.value
                node.left.value = temp
        elif child_pos == '1':
            if node.value > node.right.value:
                temp = node.value
                node.value = node.right.value
                node.right.value = temp

    def insert_list(self, xs):
        for x in xs:
            self.insert(x)

    def find_smallest(self):
        if self.is_heap_satisfied():
            return self.root.value

    def remove_min(self):
        if self.root:
            if self.size == 1:
                self.root = None
                self.size -= 1
            else:
                Heap._remove_min(self.size, self.root)
                self.size -= 1

    @staticmethod
    def _remove_min(size, node):
        pos_bin = '{0:b}'.format(size)[1:]
        last_added = None
        curr_node = node
        while pos_bin:
            if pos_bin[0] == '0':
                if len(pos_bin) == 1:
                    last_added = curr_node.left.value
                    curr_node.left = None
                    pos_bin = pos_bin[1:]
                else:
                    curr_node = curr_node.left
                    pos_bin = pos_bin[1:]
            else:
                if len(pos_bin) == 1:
                    last_added = curr_node.right.value
                    curr_node.right = None
                    pos_bin = pos_bin[1:]
                else:
                    curr_node = curr_node.right
                    pos_bin = pos_bin[1:]
        node.value = last_added
        while not Heap._is_heap_satisfied(node):
            if node.right and node.left:
                if node.right.value < node.left.value:
                    temp = node.value
                    node.value = node.right.value
                    node.right.value = temp
                    node = node.right
                else:
                    temp = node.value
                    node.value = node.left.value
                    node.left.value = temp
                    node = node.left
            elif node.right and node.left is None:
                temp = node.value
                node.value = node.right.value
                node.right.value = temp
                node = node.right
            elif node.left and node.right is None:
                temp = node.value
                node.value = node.left.value
                node.left.value = temp
                node = node.left
