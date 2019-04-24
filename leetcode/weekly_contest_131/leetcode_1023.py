import re
from functools import partial
from typing import List

class Solution:
	def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
		def queryMatchesPattern(pattern: str, query: str) -> bool:
			pattern_len = len(pattern)
			pattern_i = 0
			for char in query:
				if pattern_i < pattern_len and char == pattern[pattern_i]:
					pattern_i += 1
				elif not char.islower():
					return False
			return pattern_i == pattern_len
		queryMatches = partial(queryMatchesPattern, pattern)
		return list(map(queryMatches, queries))

soln = Solution()
assert [True,False,True,True,False] == soln.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB")
assert [True,False,True,False,False] == soln.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBa")

ans = soln.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBaT")
assert ans == [False,True,False,False,False]
