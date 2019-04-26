from heapq import nsmallest
from typing import List

class Solution:
	def twoCitySchedCost(self, costs: List[List[int]]) -> int:
		N = len(costs) // 2
		return sum(map(lambda t: t[0], costs)
			) + sum(nsmallest(N, (cost[1] - cost[0] for cost in costs)))
