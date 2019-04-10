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

soln = Solution()
root = TreeNode('a')
root.left = TreeNode('b')
root.left.left = TreeNode('d')
root.left.right = TreeNode('e')
root.right = TreeNode('c')
root.right.left = TreeNode('f')

invertedRoot = soln.invertTree(root)
assert invertedRoot.val == 'a'
assert invertedRoot.left.val == 'c'
assert invertedRoot.left.right.val == 'f'
assert invertedRoot.right.val == 'b'
assert invertedRoot.right.left.val == 'e'
assert invertedRoot.right.right.val == 'd'