class Solution:
	def readN(self, file, n: int) -> str:
		count = (n // 7) + (0 if n % 7 == 0 else 1)
		ans = ""
		for _ in range(count):
			ans += self.read7(file)
		return ans
	def read7(self, file) -> str:
		"""
		Daily Coding Problem #82: Given read7 that reads 7 chars from a file
		implement readN
		"""
		return file.read(7)

soln = Solution()

with open("problem_82_test_file.txt", 'r', encoding="utf-8") as f:
	assert "Hello World" == soln.readN(f, 11)