from random import random, randint
from itertools import accumulate
from bisect import bisect_left

class Solution:
	def __init__(self, weights):
		"""
		:type weights: List[int]
		"""
		total = sum(weights)
		cumulative_weights = list(accumulate((weight / total for weight in weights)))
		cumulative_weights[-1] = 1
		self.cumulative_weights = cumulative_weights

	def pickIndex(self):
		"""
		:rtype: int
		"""
		return bisect_left(self.cumulative_weights, random())

w = [randint(0, 100_000) for i in range(10_000)]
obj = Solution(w)
for i in range(10_000):
	print(obj.pickIndex(), end=' ')