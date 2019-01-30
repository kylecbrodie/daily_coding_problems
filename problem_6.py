from typing import Any, List

# We start the registry with None so dereferencing 'null pointer' (index 0)
# will return Python's null type None and calling get_pointer on None will
# return 'null pointer' (index 0)
_node_registry: List['XORLinkedListNode'] = [None]

def get_pointer(node: 'XORLinkedListNode') -> int:
	if node is None:
		return 0
	return node._self_ptr

def dereference_pointer(node_ptr: int) -> 'XORLinkedListNode':
	try:
		return _node_registry[node_ptr]
	except IndexError:
		return None

class XORLinkedListNode:
	def __init__(self, val: Any, prev: 'XORLinkedListNode'=None, next: 'XORLinkedListNode'=None):
		self.val = val
		self.both = get_pointer(prev) ^ get_pointer(next)
		self._self_ptr = len(_node_registry)
		self._add_self_to_node_both(prev)
		self._add_self_to_node_both(next)
		_node_registry.append(self)

	def _add_self_to_node_both(self, node: 'XORLinkedListNode') -> None:
		if node is not None:
			node.both ^= get_pointer(self)

	def _next_node(self, prev: 'XORLinkedListNode') -> 'XORLinkedListNode':
		return dereference_pointer(get_pointer(prev) ^ self.both)

	def _prev_node(self, next: 'XORLinkedListNode') -> 'XORLinkedListNode':
		return dereference_pointer(get_pointer(next) ^ self.both)

class XORLinkedList:
	head: XORLinkedListNode = None
	tail: XORLinkedListNode = None
	count: int = 0

	def add(self, val: Any) -> None:
		if self.tail is None:
			self.head = self.tail = XORLinkedListNode(val)
		else:
			old_tail = self.tail
			self.tail = XORLinkedListNode(val, prev=old_tail)
		self.count += 1
	
	def __len__(self):
		return self.count

	def get(self, index: int) -> XORLinkedListNode:
		if index < 0 or index >= self.count:
			raise IndexError('index out of range')
		closer_to_head = index <= ((self.count - 1) // 2)
		return self._get(self.head if closer_to_head else self.tail, index if closer_to_head else self.count - 1 - index)
	
	def _get(self, starting_node: XORLinkedListNode, index: int) -> XORLinkedListNode:
		if index < 0 or index >= self.count:
			raise IndexError('index out of range')
		if index == 0:
			return starting_node
		else:
			prev_node = starting_node
			node = starting_node._next_node(None)
			index -= 1
			while node is not None and index > 0:
				n = node._next_node(prev_node)
				prev_node, node = node, n
				index -= 1
			return node

xor_linked_list = XORLinkedList()
xor_linked_list.add('head')
xor_linked_list.add('next')
xor_linked_list.add('next.next')
xor_linked_list.add('next.next.next')
xor_linked_list.add('tail')

assert xor_linked_list.get(0).val == 'head'
assert xor_linked_list.get(1).val == 'next'
assert xor_linked_list.get(2).val == 'next.next'
assert xor_linked_list.get(3).val == 'next.next.next'
assert xor_linked_list.get(4).val == 'tail'