class Solution:
	# It is fibonacci!
	def climbStairs(self, n):
		if n == 0 or n == 1:
			return 1
		return self.climbStairs(n - 1) + self.climbStairs(n - 2)

soln = Solution()
assert soln.climbStairs(2) == 2
assert soln.climbStairs(4) == 5
assert soln.climbStairs(5) == 8
assert soln.climbStairs(35) == 14930352