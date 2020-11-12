from pprint import pprint

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def getHeight(root: Node):
    if (not root.left and not root.right):
        return 0
    leftHeight = getHeight(root.left) if root.left else 0
    rightHeight = getHeight(root.right) if root.right else 0

    return max(leftHeight, rightHeight) + 1


# Breadth first (level order) traversal of tree

# Recursive approach
def levelOrderRecursive(root: Node):
    height = getHeight(root)
    for level in range(height+1):
        visitNodesByLevel(root, level)


def visitNodesByLevel(root, level):
    if not root or level < 0:
        return
    if level == 0:
        print(str(root.info) + " ")
    else:
        visitNodesByLevel(root.left, level - 1)
        visitNodesByLevel(root.right, level - 1)
    return


# Dynamic programming approach. faster
def levelOrder(root: Node):
    # 1) Find height of tree.
    treeHeight = getHeight(root)
    levels = range(treeHeight+1)

    # Declare an empty dictionary.
    nodesByLevel = {}
    # Initialize nodesByLevel
    for level in levels:
        if level == 0:
            nodesByLevel[level] = [root]
        else:
            # declare an empty list.
            nodesByLevel[level] = []

    # 2) Find and separate nodes by their level in tree.
    for level in levels:
        for node in nodesByLevel[level]:
            # Add children of current node to list of next level.
            if node.left:
                nodesByLevel[level+1].append(node.left)
            if node.right:
                nodesByLevel[level+1].append(node.right)

    # Print nodes by level order.
    for level, nodes in nodesByLevel.items():
        for node in nodes:
            print(str(node.info), end=' ')


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)
