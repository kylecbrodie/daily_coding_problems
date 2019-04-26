# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

	def __repr__(self):
		return f"TreeNode(val={self.val})"

# also LeetCode 104
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
		# LeetCode 104 wants the depth number so return ans[0] instead
		return ans[1]
