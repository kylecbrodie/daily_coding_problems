# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
	def __init__(self, list_or_int):
		self.isInt = False
		self.integer = None
		self.list = None
		if type(list_or_int) == int:
			self.isInt = True
			self.integer = list_or_int
		else:
			self.list = list_or_int

	def isInteger(self):
		"""
		@return True if this NestedInteger holds a single integer, rather than a nested list.
		:rtype bool
		"""
		return self.isInt

	def getInteger(self):
		"""
		@return the single integer that this NestedInteger holds, if it holds a single integer
		Return None if this NestedInteger holds a nested list
		:rtype int
		"""
		return self.integer

	def getList(self):
		"""
		@return the nested list that this NestedInteger holds, if it holds a nested list
		Return None if this NestedInteger holds a single integer
		:rtype List[NestedInteger]
		"""
		return self.list
	
	def __repr__(self):
		return str(self.integer) if self.isInt else str(self.list)
	
class NestedIterator(object):

	def __init__(self, nestedList):
		"""
		Initialize your data structure here.
		:type nestedList: List[NestedInteger]
		"""
		self.index_stack = []
		if len(nestedList) > 0:
			self.index_stack.append((nestedList, 0))
		self._move_to_next_int()

	def _move_to_next_int(self):
		self.next_int = None
		while len(self.index_stack) > 0:
			list_, list_index = self.index_stack.pop()
			nested_integer = list_[list_index]
			if nested_integer.isInteger():
				self.next_int = nested_integer.getInteger()
				if list_index + 1 < len(list_):
					self.index_stack.append((list_, list_index + 1))
				break
			else:
				nested_list = nested_integer.getList()
				if list_index + 1 < len(list_):
					self.index_stack.append((list_, list_index + 1))
				if len(nested_list) > 0:
					self.index_stack.append((nested_list, 0))
				

	def next(self):
		"""
		:rtype: int
		"""
		ans = self.next_int
		self._move_to_next_int()
		return ans

	def hasNext(self):
		"""
		:rtype: bool
		"""
		return self.next_int is not None
		
def _build_nested_list(list_):
	for i in range(len(list_)):
		if type(list_[i]) is list:
			list_[i] = NestedInteger(_build_nested_list(list_[i]))
		else:
			list_[i] = NestedInteger(list_[i])
	return list_

nestedList = _build_nested_list([[1, 1], 2, [1, 1]])
# Your NestedIterator object will be instantiated and called as such:
i, v = NestedIterator(nestedList), []
while i.hasNext(): v.append(i.next())

assert [1, 1, 2, 1, 1] == v