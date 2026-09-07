class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, num=3, leftInc=1, rightInc=2):
        self.root = Node(0)
        self.num = num
        self.leftInc = leftInc
        self.rightInc = rightInc

    def populate_node(self, node):
        if node.left is None:
            node.left = Node(node.data + self.leftInc)
        if node.right is None:
            node.right = Node(node.data + self.rightInc)

    def build_tree(self):
        # Initialized locally instead of in __init__
        queue = [self.root]

        while len(queue) != 0:
            node = queue.pop(0)
            self.populate_node(node)
            if node.left.data < self.num:
                queue.append(node.left)
            if node.right.data < self.num:
                queue.append(node.right)


    def pretty_print(self):
        def _p(n, p="", l=True, r=True):
            if not n: return
            _p(n.right, p + ("│   " if l else "    "), False, False)
            print(p + (str(n.data) if r else ("└── " if l else "┌── ") + str(n.data)))
            _p(n.left, p + ("    " if l else "│   "), True, False)
        _p(self.root)

# --- Test it out ---
if __name__ == "__main__":
    tree = BinaryTree(5, 1, 2)
    tree.build_tree()
    tree.pretty_print()