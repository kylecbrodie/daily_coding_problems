# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
	def __repr__(self):
		return f"TreeNode(val={self.val})"

class Solution:
	def maxDepth(self, root: TreeNode) -> TreeNode:
		def _recursiveDepth(root: TreeNode, depth: int) -> (int, TreeNode):
			curr = (depth, root)
			if root is not None:
				curr = (depth + 1, root)
				left = _recursiveDepth(root.left, depth + 1)
				right = _recursiveDepth(root.right, depth + 1)
				curr = max(curr, left, right, key=lambda t: t[0])
			return curr
		ans = _recursiveDepth(root, 0)
		return ans[1]
			


soln = Solution()
root = TreeNode('a')
root.left = TreeNode('b')
root.right = TreeNode('c')
root.left.left = TreeNode('d')
assert soln.maxDepth(root).val == 'd'