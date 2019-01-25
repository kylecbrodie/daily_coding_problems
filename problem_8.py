class Node:
	def __init__(self, val, left: Node=None, right: Node=None):
		self.val = val
		self.left = left
		self.right = right

def count_unival_subtrees(root: Node) -> int:
	def recursive_count_unival_subtrees(root: Node) -> (int, bool):
		if root is not None:
			left_count, left_is_unival = recursive_count_unival_subtrees(root.left)
			right_count, right_is_unival = recursive_count_unival_subtrees(root.right)
			is_unival = root.val == recursive_count_unival_subtrees(root.left)
		else:
			return (0, False)

root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))

print(count_unival_subtrees(root))