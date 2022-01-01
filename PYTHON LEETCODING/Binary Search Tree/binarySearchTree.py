class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def empty(self):
        if (self.root == None):
            return True
        else:
            return False

    def insert(self, value):
        newNode = TreeNode(value)
        if (self.empty()):
            self.root = newNode
        else:
            it_parent = TreeNode()
            it = self.root

            while (it != None):
                it_parent = it
                if (value < it.val):
                    it = it.left
                elif (value > it.val):
                    it = it.right

            if (value < it_parent.val):
                it_parent.left = newNode
            elif (value > it_parent.val):
                it_parent.right = newNode

    def inorder(self, node):  # LVR
        if (node == None):
            return
        else:
            self.inorder(node.left)
            print(node.val)
            self.inorder(node.right)


if (__name__ == "__main__"):
    entityTree = BinarySearchTree()

    print(f"Is entity tree empty? {entityTree.empty()}")

    # Inserting elements
    entityTree.insert(5)
    entityTree.insert(3)
    entityTree.insert(1)
    entityTree.insert(6)
    entityTree.insert(10)
    entityTree.insert(8)
    entityTree.insert(11)

    print(f"Is entity now tree empty? {entityTree.empty()}")

    entityTree.inorder(entityTree.root)
