import unittest
from unittest import TestCase

from daily_coding_problems.leetcode.weekly_contest_133 import (
	leetcode_1029 as l1029,
	leetcode_1030 as l1030,
	leetcode_1032 as l1032,
)

class TestLeetCode1029(TestCase):
	def setUp(self):
		self.soln = l1029.Solution()

	def test_twoCitySchedCost(self):
		self.assertEqual(
			1859,
			self.soln.twoCitySchedCost([[259, 770], [448, 54], [926, 667],
			[184, 139], [840, 118], [577, 469]])
		)
