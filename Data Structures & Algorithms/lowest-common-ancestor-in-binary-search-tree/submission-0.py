# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if (root.val == p and ((root.left.val == q) or (root.right.val == q))):
        #     return root.val
        # elif (root.val == q and ((root.left.val == p) or (root.right.val == p))):
        #     return root.val
        # elif ((root.left.val == p) and (root.right.val == q) or (root.left.val == q) and (root.right.val == p)):
        #     return root.val
        if ((int(q.val) > int(root.val)) and (int(p.val) > int(root.val))):
            print("RIGHT")
            return self.lowestCommonAncestor(root.right, p, q)
        elif ((int(q.val) < int(root.val)) and (int(p.val) < int(root.val))):
            print("LEFT")
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            # print("HI")
            # print(root.val)
            return root
            
