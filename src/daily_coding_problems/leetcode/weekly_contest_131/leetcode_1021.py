class Solution:
	def removeOuterParentheses(self, S: str) -> str:
		reduced_s = ""
		current_prim_starting_i = 0
		depth = 1
		for i in range(1, len(S)):
			depth += -1 if S[i] == ')' else 1
			if depth == 0:
				# primative found
				reduced_prim_start = current_prim_starting_i + 1
				reduced_prim_end = i
				# add to answer
				reduced_s += S[reduced_prim_start:reduced_prim_end]
				# move prim starting point to after the end of the current prim
				current_prim_starting_i = i+1
		return reduced_s

soln = Solution()
assert "()()()" == soln.removeOuterParentheses("(()())(())")
assert "()()()()(())" == soln.removeOuterParentheses("(()())(())(()(()))")
assert "" == soln.removeOuterParentheses("()()")
assert "" == soln.removeOuterParentheses("")
