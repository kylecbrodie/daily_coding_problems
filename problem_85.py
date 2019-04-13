class Solution:
	def select(self, x: int, y: int, b: int) -> int:
		return b * x + (1-b) * y

soln = Solution()
assert 12342362356 == soln.select(12342362356, 98033456087, 1)
assert 98033456087 == soln.select(12342362356, 98033456087, 0)