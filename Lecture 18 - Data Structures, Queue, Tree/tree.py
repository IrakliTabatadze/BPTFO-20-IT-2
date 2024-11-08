class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node

    def printParents(self):
        print('The parents of each node are: ')
        self._printParents(self.root, None)

    def _printParents(self, node, parentNode):
        if node is not None:
            if parentNode is None:
                print(node.key, '-> Root')
            else:
                print(node.key, '->', parentNode.key)

            self._printParents(node.left, node)
            self._printParents(node.right, node)


tree = BinaryTree()

tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(14)
tree.insert(16)
tree.insert(9)
tree.insert(4)

#      10
#     /   \
#    5      15
#  /  \     / \
# 4     9   14  16

# 10 -> Root
# 5 -> 10
# 15 -> 10
# 4 -> 5
# 9 -> 5
# 14 -> 15
# 16 -> 15

tree.printParents()
