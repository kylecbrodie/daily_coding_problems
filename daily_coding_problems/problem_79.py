from typing import List

# also LeetCode 665
class Solution:
	def checkPossibility(self, nums: List[int]) -> bool:
		# Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.
		# For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.
		# Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.
		if nums is None or len(nums) == 0:
			return False

		patched = False

		for i in range(0, len(nums)-1):
			if nums[i] > nums[i+1]:
				if not patched:
					if i-1 < 0 or nums[i-1] <= nums[i+1]:
						nums[i] = nums[i+1]
					else:
						nums[i+1] = nums[i]
					patched = True
				else:
					return False

		return True

soln = Solution()

assert not soln.checkPossibility([3,4,2,3])
assert soln.checkPossibility([4,2,3])