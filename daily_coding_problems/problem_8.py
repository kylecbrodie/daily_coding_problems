class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def count_unival_subtrees(root: Node) -> int:
	def recursive_count_unival_subtrees(node: Node) -> (int, bool):
		if node is None:
			return 0, True
		left_count, left_is_unival = recursive_count_unival_subtrees(node.left)
		right_count, right_is_unival = recursive_count_unival_subtrees(node.right)
		count = left_count + right_count
		if left_is_unival and right_is_unival \
		and (node.left is None or node.left.val == node.val) \
		and (node.right is None or node.right.val == node.val):
			return count + 1, True
		return count, False

	count, _ = recursive_count_unival_subtrees(root)
	return count

root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
root2 = Node(0, Node(0), Node(0, Node(0, Node(0), Node(0)), Node(0)))
root3 = Node('a', Node('a'), Node('a', Node('a'), Node('a', right=Node('A'))))
root4 = Node('a', Node('c'), Node('b', Node('b'), Node('b', right=Node('b'))))

print(count_unival_subtrees(root))
print(count_unival_subtrees(root2))
print(count_unival_subtrees(root3))
print(count_unival_subtrees(root4))