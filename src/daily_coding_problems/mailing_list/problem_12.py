from math import factorial

class Solution:
	def climbStairs(self, n):
		# initialize with 1 for the n 1-step way
		distinct_ways = 0
		# iterate from zero 2's up to the max integer
		# multiple of 2's
		for num_twos in range((n // 2) + 1):
			# The list of integers that sums to n will contain
			# num_twos 2's and max(n - 2*num_twos, 0) 1's
			num_integers = num_twos + max(n - 2 * num_twos, 0)
			distinct_ways += factorial(num_integers) // (
				factorial(num_twos) * factorial(num_integers - num_twos)
			)
		return distinct_ways
