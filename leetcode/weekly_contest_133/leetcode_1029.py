from typing import List
from heapq import nsmallest

class Solution:
	def twoCitySchedCost(self, costs: List[List[int]]) -> int:
		N = len(costs) // 2
		return sum(map(lambda t: t[0], costs)) + sum(nsmallest(N, (cost[1] - cost[0] for cost in costs)))

soln = Solution()
assert 1859 == soln.twoCitySchedCost([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]])
