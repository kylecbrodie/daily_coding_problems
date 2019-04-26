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
