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
