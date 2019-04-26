from heapq import (
	heappop,
	heappush,
	heappushpop,
	heapreplace,
	merge,
)
from typing import (
	Any,
	List,
)

class _ListNodeIterator:
	def __init__(self, curr_node):
		self.curr_node = curr_node

	def __iter__(self):
		return self

	def __next__(self):
		if self.curr_node is not None:
			ans = self.curr_node
			self.curr_node = self.curr_node.next
			return ans
		else:
			raise StopIteration()

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

	def __iter__(self):
		return _ListNodeIterator(self)

	def __repr__(self):
		return f"ListNode({self.val})->{self.next}"

# also leetcode 23
class Solution:
	def mergeKLists(self, lists: List[ListNode]) -> ListNode:
		head = None
		prev_node = None

		if len(lists) == 0:
			return None
		elif len(lists) == 1:
			return lists[0]

		while len(lists) > 1:
			min_index = 0
			min_node = lists[0]

			for i, node in enumerate(lists[1:], start=1):
				if node is not None and (
					min_node is None or node.val <= min_node.val
				):
					min_index = i
					min_node = node

			if lists[min_index] is None or lists[min_index].next is None:
				del lists[min_index]
			else:
				lists[min_index] = lists[min_index].next

			if min_node is not None:
				min_node.next = None
				if prev_node is not None:
					prev_node.next = min_node
				prev_node = min_node
				if head is None:
					head = prev_node

		if prev_node is not None:
			prev_node.next = lists[0]

		return head

	def mergeKListsSimplest(self, lists):
		root = ListNode(None)
		curr_node = root

		for i in range(len(lists)):
			if not lists[i]:
				lists[i] = []

		for node in merge(*lists, key=lambda n: n.val):
			curr_node.next = node
			curr_node = node

		return root.next

	def mergeKListsHeap(self, lists: List[ListNode]) -> ListNode:
		root = ListNode(None)
		curr_node = root
		k_heap = []

		for i, list_head in enumerate(lists):
			if list_head:
				heappush(k_heap, (list_head.val, i, list_head))

		while len(k_heap) > 0:
			_, i, node = k_heap[0]
			curr_node.next = node
			curr_node = node
			if node.next:
				heapreplace(k_heap, (node.next.val, i, node.next))
			else:
				heappop(k_heap)

		return root.next

	def mergeKListsFastest(self, lists: List[ListNode]) -> ListNode:
		root = ListNode(None)
		curr_node = root
		nodes = []

		for list_head in lists:
			while list_head is not None:
				nodes.append(list_head)
				list_head = list_head.next

		for node in sorted(nodes, key=lambda n: n.val):
			curr_node.next = node
			curr_node = node

		return root.next

# Given k sorted singly linked lists,
# write a function to merge all the lists
# into one sorted singly linked list.

soln = Solution()
n1 = ListNode(1)
n3 = ListNode(3)
n6 = ListNode(6)
n1.next = n3
n3.next = n6

n2 = ListNode(2)
n4 = ListNode(4)
n5 = ListNode(5)
n2.next = n4
n4.next = n5

print(n1)
print(n2)
print(soln.mergeKLists([n1, n2]))

print(soln.mergeKLists([None]))
print(soln.mergeKLists([None, None]))

# [[],[-1,5,11],[],[6,10]]
nNegOne = ListNode(-1)
n5Again = ListNode(5)
n11 = ListNode(11)
nNegOne.next = n5Again
n5Again.next = n11

n6Again = ListNode(6)
n10 = ListNode(10)
n6Again.next = n10

print(soln.mergeKLists([None, nNegOne, None, n6Again]))

nNegOne = ListNode(-1)
n5Again = ListNode(5)
n11 = ListNode(11)
nNegOne.next = n5Again
n5Again.next = n11

n6Again = ListNode(6)
n10 = ListNode(10)
n6Again.next = n10

print(soln.mergeKListsSimplest([None, nNegOne, None, n6Again]))

nNegOne = ListNode(-1)
n5Again = ListNode(5)
n11 = ListNode(11)
nNegOne.next = n5Again
n5Again.next = n11

n6Again = ListNode(6)
n10 = ListNode(10)
n6Again.next = n10

print(soln.mergeKListsHeap([None, nNegOne, None, n6Again]))

nNegOne = ListNode(-1)
n5Again = ListNode(5)
n11 = ListNode(11)
nNegOne.next = n5Again
n5Again.next = n11

n6Again = ListNode(6)
n10 = ListNode(10)
n6Again.next = n10

print(soln.mergeKListsFastest([None, nNegOne, None, n6Again]))
