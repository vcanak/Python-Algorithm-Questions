# Structure of a Tree Node
""" 
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, 
is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.
"""
class node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
def countNodes(root):
        if not root:
            return 0
        leftDepth = getDepth(root.left) # 3
        print("left: ", leftDepth)
        rightDepth = getDepth(root.right) #2
        print("right: ", rightDepth)
        print("*****")
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + countNodes(root.right)
        else:
            return pow(2, rightDepth) + countNodes(root.left)
    
def getDepth(root):
    if not root:
        return 0
    return 1 + getDepth(root.left)
        

# Driver code
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(9)
root.right.right = node(8)
root.left.left.left = node(6)
root.left.left.right = node(7)
print(countNodes(root))

""" 
         1
    2       3
  4    5   9    8
6   7
"""