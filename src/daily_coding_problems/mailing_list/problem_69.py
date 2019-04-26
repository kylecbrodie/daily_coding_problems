import operator as op
from functools import reduce
from heapq import nlargest, nsmallest
from itertools import chain, combinations
from typing import List

# Also LeetCode 628
class Solution:
	def maximumProduct(self, nums: List[int]) -> int:
		three_largest = nlargest(3, nums)
		# When len(nums) < 6 the three largest and the three smallest overlap
		# and the triples generated will be incorrect as some of the numbers
		# will appear more than once. We fix this by finding the n smallest
		# where n is between 0 and 3.
		n = min(max(len(nums) - 3, 0), 3)
		n_smallest = []
		if n == 1:
			n_smallest.append(min(nums))
		elif n > 1:
			n_smallest = nsmallest(n, nums)

		return max(
			map(
			lambda t: reduce(op.mul, t),
			combinations(chain(n_smallest, three_largest), 3)
			)
		)
