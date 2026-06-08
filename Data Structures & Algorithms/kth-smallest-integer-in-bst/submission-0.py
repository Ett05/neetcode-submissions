# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # while root.left:
        #     root = root.left
        # print(root.val)
        
        # if root.left:
        #     return self.kthSmallest(root.left, k-1)
        # elif root.right:
        #     return self.kthSmallest(root.right, k-1)
        # if k == 1:
        #     return root.val
        # else:
        #     return -1
        # stack = [root]
        # counter = 0
        # while counter!=k:
        #     print([val.val for val in stack])
        #     new_root = stack.pop()
        #     print(new_root.val)
        #     if not new_root:
        #         break
        #     if new_root.right:
        #         stack.append(new_root.right)
        #     if new_root.left:
        #         stack.append(new_root.left)
        #     counter += 1

        # # print([val.val for val in stack])
        # return stack[-1].val
        # counter = 0
        # stack = []
        # cur = root
        # while cur and stack:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     counter += 1
        #     if counter == k:
        #         return cur.val
        #     print(cur)
        #     print(stack)
        #     cur = cur.right
        stack = []
        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            
            curr = curr.right