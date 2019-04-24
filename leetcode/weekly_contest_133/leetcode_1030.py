from typing import List
from functools import partial

class Solution:
	def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
		def manhattanDistance(point0: List[int], point1: List[int]):
			r0, c0 = point0
			r1, c1 = point1
			return abs(r0 - r1) + abs(c0 - c1)

		manhattanDistanceToOrigin = partial(manhattanDistance, [r0, c0])

		return list(sorted(([r, c] for c in range(C) for r in range(R)), key=manhattanDistanceToOrigin))
