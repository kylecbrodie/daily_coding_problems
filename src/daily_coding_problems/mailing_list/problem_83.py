class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	def __repr__(self):
		return f"TreeNode({self.val})"

# @lc app=leetcode id=226 lang=python3
class Solution:
	def invertTree(self, root: 'TreeNode') -> 'TreeNode':
		def _recursiveInvertTree(root):
			if root is not None:
				root.left, root.right = root.right, root.left
				if root.left is not None:
					_recursiveInvertTree(root.left)
				if root.right is not None:
					_recursiveInvertTree(root.right)

		_recursiveInvertTree(root)
		return root
