# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def computeLeafSum(self,root,level,d):
        if not root:
            return d
        if level in d:
            d[level] = (d[level]+root.val)
        else:
            d[level] = root.val
        self.computeLeafSum(root.left,level+1,d)
        self.computeLeafSum(root.right,level+1,d)
        return d
        
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        d = self.computeLeafSum(root,0,{})
        lst = list(d.items())
        res = [j for i,j in lst]
        return res[-1]
    