# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root==None:
            return []
        ans=[]
        curr=[]
        curr.append(root)
        while(len(curr)>0):
            s = []
            prev = []
            for i in curr:
                s.append(i.val)
                if i.left is not None:
                    prev.append(i.left)
                if i.right is not None:
                    prev.append(i.right)
            ans.append(s)
            curr = prev
        return reversed(ans)
