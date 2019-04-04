from dataclasses import dataclass
from typing import List

@dataclass
class Interval:
	start: int = 0
	end: int = 0

# Also LeetCode problem 56
class Solution:
	def merge(self, intervals: List[Interval]) -> List[Interval]:
		"""
		Returns a new list of intervals where overlapping intervals from the
		given list are merged into one interval. Neither the given nor the
		returned list should be assumed to be ordered in any way. The given
		list may be modified.
		"""
		intervals.sort(key=lambda i: i.start)

		nonoverlapping_intervals = []

		for interval in intervals:
			if len(nonoverlapping_intervals) == 0 \
			   or nonoverlapping_intervals[-1].end < interval.start:

				nonoverlapping_intervals.append(interval)
			else:
				nonoverlapping_intervals[-1].end = max(nonoverlapping_intervals[-1].end, interval.end)

		return nonoverlapping_intervals

soln = Solution()
assert [Interval(1, 3), Interval(4, 10), Interval(20, 25)] == soln.merge([Interval(1, 3), Interval(5, 8), Interval(4, 10), Interval(20, 25)])

# everything overlaps
assert [Interval(1, 10)] == soln.merge([Interval(i, i+2) for i in range(1, 9)])

# failed LeetCode test case
assert [Interval(1, 10)] == soln.merge([Interval(2,3),Interval(4,5),Interval(6,7),Interval(8,9),Interval(1,10)])

# failed LeetCode test case 2
assert [Interval(0, 5)] == soln.merge([Interval(4, 5), Interval(1, 4), Interval(0, 1)])

# failed LeetCode test case 3
assert [Interval(1, 4)] == soln.merge([Interval(1, 4), Interval(1, 4)])