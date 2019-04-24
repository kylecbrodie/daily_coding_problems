# Copyright (c) 2019 Dymonchyk

# NOT MY SOLUTION
# This is Dymonchyk's solution but converted from C++ to Python

from typing import List

class Solution:
	def videoStitching(self, clips: List[List[int]], T: int) -> int:
		last = 0
		cnt = 0
		while True:
			if last >= T:
				break

			found = False
			mx = -1
			for i in range(len(clips)):
				if (clips[i][0] <= last):
					mx = max(mx, clips[i][1])

			if (mx > last):
				last = mx
				cnt += 1
				found = True

			if not found:
				break

		if last >= T:
			return cnt
		return -1

soln = Solution()
assert 3 == soln.videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10)
assert -1 == soln.videoStitching([[0,1],[1,2]], 5)
assert 3 == soln.videoStitching([[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], 9)
assert 2 == soln.videoStitching([[0,4],[2,8]], 5)
