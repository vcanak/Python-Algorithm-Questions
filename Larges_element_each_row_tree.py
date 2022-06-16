"""
Given the root of a binary tree, 
return an array of the largest value in each row of the tree (0-indexed).
"""
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def get_max_rec(res,root,level):
    if (not root):
        return
    if (level == len(res)):
        res.append(root.val)
    else:
        res[level] = max(res[level],root.val)
    
    #Recursiveyly traverse tree left and right
    get_max_rec(res,root.left,level+1)
    get_max_rec(res, root.right,level+1)
    
def get_max_element(root):
    res = []
    get_max_rec(res, root, 0)
    return res

root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)
print(get_max_element(root))  
    