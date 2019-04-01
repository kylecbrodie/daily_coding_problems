class Solution:
	def countOccurancesInMultTable(self, n: int, x: int) -> int:
		"""
		n: int - size of multiplication table
		x: int - target number to count occurances

		return number of occurances of x
		"""
		occurances = 0
		# for i from 1 to n (inclusive)
		for i in range(1, n+1):
			# if i divides x
			if x % i == 0:
				other_factor = x // i
				# if the other factor is in our table
				if other_factor <= n:
					occurances += 1
		return occurances

soln = Solution()
assert 4 == soln.countOccurancesInMultTable(6, 12)