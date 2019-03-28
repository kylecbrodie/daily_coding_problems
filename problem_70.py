from itertools import dropwhile, product, chain, repeat

class Solution:
	def _digitListToNum(self, digits, largestFirst=True):
		num = 0
		n = len(digits)
		powers = range(n-1, -1, -1) if largestFirst else range(n)
		for digit, power in zip(digits, powers):
			num += digit * 10**power
		return num

	def perfectNumbers(self):
		num_digits = 2
		while True:
			# The highest digit in a number can vary between 1 and 9 and lower
			# digits can vary from 0 to 9
			variable_digits_ranges = chain([range(1, 10)], repeat(range(10), num_digits - 2))
			# There are (num_digits - 1) digits that can vary in a perfect number
			# since the last digit must be the digit such that the sum of the
			# digits equals 10
			for digits in product(*variable_digits_ranges):
				digit_list = list(digits)
				determined_digit = 10 - sum(digit_list)
				digit_list.append(determined_digit)
				yield self._digitListToNum(digit_list)

			num_digits += 1

	def nthPerfectNumber(self, n):
		"""
		A number is considered perfect if its digits sum up to exactly 10
		"""
		_, nth_perfect_number = next(dropwhile(lambda t: t[0] < n, enumerate(self.perfectNumbers(), start=1)))
		return nth_perfect_number

soln = Solution()
assert 109 == soln.nthPerfectNumber(10)