# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = [float("-inf")]
        self.maxPath(root, res)
        return res[0]
        
        
    def maxPath(self, root, res):
        if not root:
            return 0
        
        left = max(self.maxPath(root.left, res), 0)
        right = max(self.maxPath(root.right, res), 0)
        
        res[0] = max(res[0], root.val + left + right)
        
        return max(root.val + left, root.val + right)

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxSum = [float("-inf")]
        self.pathSum(root, maxSum)
        return maxSum[0]
        
    def pathSum(self, node, maxSum):
        if not node:
            return 0
        
#         left = max(0, self.pathSum(node.left, maxSum))
#         right = max(0, self.pathSum(node.right, maxSum))
        left = self.pathSum(node.left, maxSum)
        right = self.pathSum(node.right, maxSum)
        
#         maxSum[0] = max(maxSum[0], left + right + node.val)
        curMax = max(left + node.val, right + node.val, node.val, left+right+node.val)
        maxSum[0] = max(maxSum[0], curMax)
        
        # return max(left, right) + node.val
        return max(left + node.val, right + node.val, node.val)