class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(root, clone):
            if not root:
                return None
            if root == target:
                return clone
            l = dfs(root.left, clone.left)
            if l:
                return l
            r = dfs(root.right, clone.right)
            if r:
                return r
            return None
        return dfs(original, cloned)