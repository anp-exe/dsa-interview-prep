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

    def build_tree(self):
        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if self.num > current.data:
                if current.left is None:
                    current.left = Node(current.data + self.leftInc)
                if current.right is None:
                    current.right = Node(current.data + self.rightInc)

            queue.append(current.left)
            queue.append(current.right)

    def pretty_print(self):
        def _p(n, p="", l=True, r=True):
            if not n: return
            _p(n.right, p + ("│   " if l else "    "), False, False)
            print(p + (str(n.data) if r else ("└── " if l else "┌── ") + str(n.data)))
            _p(n.left, p + ("    " if l else "│   "), True, False)
        _p(self.root)

# --- Test it out ---
if __name__ == "__main__":
    tree = BinaryTree(6, 1, 2)
    tree.build_tree()
    tree.pretty_print()