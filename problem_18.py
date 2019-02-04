from itertools import repeat

class Solution:
	def subarrayMaxima(self, arr, k):
		k_less_one = k - 1
		lookaside = list(repeat(0, k))
		for i, elem in enumerate(arr):
			index = i % k
			lookaside[index] = elem
			if i >= k_less_one:
				yield max(lookaside)

soln = Solution()
assert [10, 7, 8, 8] == list(soln.subarrayMaxima([10, 5, 2, 7, 8, 7], 3))
