class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class BTreeData:
	def __init__(self, n: Node, isTarget: bool):
		self.n = n
		self.isTarget = isTarget

class Solution:
	def findSecondLargest(self, root: Node) -> Node:
		return self._helper(root).n

	def findSecondLargest2(self, root: Node) -> Node:
		if root.right is not None:
			secondGreatestInRightSubtree = self.findSecondLargest2(root.right)
			if secondGreatestInRightSubtree is None:
				return root
			else:
				return secondGreatestInRightSubtree
		else:
			if root.left is not None:
				return root.left
			else:
				return None

	def _helper(self, n: Node) -> BTreeData:
		if n.right is not None:
			data = self._helper(n.right)
			if data.isTarget == False:
				data = BTreeData(n, True)
			return data
		else:
			return BTreeData(None, False
				) if n.left is None else BTreeData(n.left, True)
