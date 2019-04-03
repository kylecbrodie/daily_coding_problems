# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Input: [2,2,1]
# Output: 1

# Input: [4,1,2,1,2]
# Output: 4 

# Input: [1,1,4,4,6,6,7]
# Output: 7 Space: O(n) O(n/2) => O(n)
class Solution:
	def findSingularElement(self, integers):
		uniqueness_set = set()
		for i in range(len(integers)):
			if integers[i] in uniqueness_set:
				uniqueness_set.remove(integers[i])
			else:
				uniqueness_set.add(integers[i])
		return uniqueness_set.pop()

	def findSingularElement2(self, integers):
		singular_element = 0
		for i in range(len(integers)):
			singular_element = singular_element ^ integers[i]
		return singular_element

# 2∗(a+b+c)−(a+a+b+b+c)=c (for the math solution)

#class Solution(object):
#    def singleNumber(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: int
#        """
#        return 2 * sum(set(nums)) - sum(nums)

soln = Solution()
print(soln.findSingularElement([2,2,1]))
print(soln.findSingularElement([4,1,2,1,2]))

print(soln.findSingularElement2([2,2,1]))
print(soln.findSingularElement2([4,1,2,1,2]))
print(soln.findSingularElement2([1,1,4,4,6,6,7]))