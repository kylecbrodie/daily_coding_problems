class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def serialize(root):
	"""
	Serialize a binary tree in depth first, left first order. We assume node values
	do not contain the comma character.
	"""
	def dfs_preorder(root):
		nodes_to_visit = [root]
		while len(nodes_to_visit) > 0:
			node = nodes_to_visit.pop(0)
			if node is not None:
				nodes_to_visit.insert(0, node.left)
				nodes_to_visit.insert(1, node.right)
			yield node

	return ','.join((node.val if node is not None else 'None' for node in dfs_preorder(root)))
	
def deserialize(serialized_tree):
	def recursive_deserialize(nodeValues):
		nodeValue = nodeValues.pop(0)
		if nodeValue == 'None':
			return None
		root = Node(nodeValue)
		root.left = recursive_deserialize(nodeValues)
		root.right = recursive_deserialize(nodeValues)
		return root
	if len(serialized_tree) > 0:
		nodeValues = serialized_tree.split(',')
		return recursive_deserialize(nodeValues)
	return None

root = Node('root', Node('left', Node('left.left')), Node('right'))

print(serialize(root))

root2 = deserialize(serialize(root))

assert root2.left.left.val == 'left.left'