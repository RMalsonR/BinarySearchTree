class Node(object):
    value = None
    left_child = None
    right_child = None

    def __init__(self, value, left=None, right=None):
        self.value = value
        if left:
            self.left_child = left
        if right:
            self.right_child = right

    def __str__(self):
        return self.value

    def has_left(self):
        return True if self.left_child else False

    def has_right(self):
        return True if self.right_child else False


class BinaryTree(object):
    root: Node = None

    def __init__(self, node: Node = None):
        if not self.root and node:
            self.root = node

    def __add__(self, node: Node, parent: Node = None):
        if not self.root:
            self.__init__(node=node)
        else:
            if parent:
                if parent.value >= node.value:
                    if parent.has_right():
                        self.__add__(node=node, parent=parent.right_child)
                    else:
                        parent.right_child = node
                else:
                    if parent.has_left():
                        self.__add__(node=node, parent=parent.left_child)
                    else:
                        parent.left_child = node
            else:
                self.__add__(node=node, parent=self.root)

    def search_back(self, number, node: Node, level_count):
        if number == node.value:
            return level_count, True
        else:
            if number < node.value:
                if node.has_left():
                    self.search_back(number=number, node=node.left_child, level_count=level_count + 1)
                else:
                    return False
            else:
                if node.has_right():
                    self.search_back(number=number, node=node.right_child, level_count=level_count + 1)
                else:
                    return False

    def search(self, number):
        return self.search_back(number=number, node=self.root, level_count=0)

    def print_level(self, level_count, node: Node, result: list):
        if not node:
            return
        else:
            if level_count == 0:
                result.append(node)
            self.print_level(level_count=level_count - 1, node=node.left_child, result=result)
            self.print_level(level_count=level_count - 1, node=node.right_child, result=result)

    def print_tree(self, result: list, node: Node):
        result.append(node)
        if node.has_left():
            self.print_tree(result=result, node=node.left_child)
        elif node.has_right():
            self.print_tree(result=result, node=node.right_child)

    def height(self, node: Node):
        if not node:
            return 0
        else:
            if node.has_left():
                l_height = self.height(node=node.left_child)
            else:
                l_height = -1
            if node.has_right():
                r_height = self.height(node=node.right_child)
            else:
                r_height = -1
            max_height = l_height if l_height > r_height else r_height
            return max_height + 1

    def to_array_values(self, result: list, node: Node):
        result.append(node.value)
        if node.has_left():
            self.to_array_values(result=result, node=node.left_child)
        elif node.has_right():
            self.to_array_values(result=result, node=node.right_child)

    def to_array_nodes(self, result: list, node: Node):
        result.append(node)
        if node.has_left():
            self.to_array_values(result=result, node=node.left_child)
        elif node.has_right():
            self.to_array_values(result=result, node=node.right_child)


def join_trees(bst_1: BinaryTree, bst_2: BinaryTree):
    tree_array_1 = []
    tree_array_2 = []
    bst_1.to_array_values(tree_array_1, bst_1.root)
    bst_2.to_array_values(tree_array_2, bst_2.root)
    result_array = [*tree_array_1, *tree_array_2]
    bst_result = BinaryTree()
    for item in result_array:
        node = Node(item)
        bst_result.__add__(node=node)
    return bst_result
