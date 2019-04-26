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
				nonoverlapping_intervals[-1].end = max(
					nonoverlapping_intervals[-1].end, interval.end
				)

		return nonoverlapping_intervals
