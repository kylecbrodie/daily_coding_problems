from typing import List
from functools import reduce

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def sumRootToLeaf(self, root: TreeNode) -> int:
		def PrefixDFSRecursiveSum(node: TreeNode, num_thus_far: int, nums: List[int]):
			"""
			Given a node, adds this node's bit to the number thus far and if
			this is a leaf node, it adds the number thus far modulo 10^9 +7
			to the list of numbers
			"""
			# node.val should be node.val mod (10^9 + 7) but since it is 1 or 0 the
			# mod will be 1 or 0 so we can skip that computation
			num_thus_far = ((num_thus_far << 1) % (10**9 + 7) + node.val) % (10**9 + 7)
			if node.left is None and node.right is None:
				# leaf node
				nums.append(num_thus_far)
			else:
				if node.left is not None:
					PrefixDFSRecursiveSum(node.left, num_thus_far, nums)
				if node.right is not None:
					PrefixDFSRecursiveSum(node.right, num_thus_far, nums)
		nums = []
		PrefixDFSRecursiveSum(root, 0, nums)
		return reduce(lambda n1, n2: ((n1 % (10**9 + 7)) + (n2 % (10**9 + 7))) % (10**9 + 7), nums, 0)

soln = Solution()
root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

assert 22 == soln.sumRootToLeaf(root)
