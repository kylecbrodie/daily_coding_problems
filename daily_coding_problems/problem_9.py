class Solution:
	def largestNonAdjacentSum(self, arr: [int]):
		if len(arr) == 0:
			return 0
		if len(arr) == 1:
			return arr[0]
		if len(arr) == 2:
			return max(arr[0], arr[1])
		
		ppLS = arr[0]
		pLS = max(arr[0], arr[1])

		for i in range(2, len(arr)):
			newLS = max(pLS, arr[i] + ppLS)
			ppLS, pLS = pLS, newLS
		return pLS

soln = Solution()

list1 = [2, 4, 6, 2, 5]
assert soln.largestNonAdjacentSum(list1) == 13

list2 = [5, 1, 1, 5]
assert soln.largestNonAdjacentSum(list2) == 10