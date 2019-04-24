from typing import List
from itertools import product
from functools import partial, reduce
import operator as op

# @lc app=leetcode id=200 lang=python3
class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		if not grid:
			return 0
		height = len(grid)
		if height == 1:
			# optimization for one row
			count = int(grid[0][0])
			for x in range(1, len(grid[0])):
				if grid[0][x-1] == '0' and grid[0][x] == '1':
					count += 1
			return count
		else:
			width = len(grid[0])
			if width == 1:
				# optimization for one column
				count = int(grid[0][0])
				for y in range(1, height):
					if grid[y-1][0] == '0' and grid[y][0] == '1':
						count += 1
				return count
			else:
				# main algorithm
				num_islands = 0

				grid_at = partial(lambda g, t: g[t[1]][t[0]], grid)

				visited = set()
				not_visited = partial(filter, lambda t: t not in visited)

				for coords in not_visited(product(range(width), range(height))):
					visited.add(coords)
					if grid_at(coords) == '1':
						num_islands += 1
						exploratory_stack = [coords]
						while len(exploratory_stack) > 0:
							x, y = exploratory_stack.pop()
							for adj_coords in not_visited([(max(0, x-1), y),
														(min(x+1, width-1), y),
														(x, max(0, y-1)),
														(x, min(y+1, height-1))]):
								visited.add(adj_coords)
								if grid_at(adj_coords) == '1':
									exploratory_stack.append(adj_coords)
				return num_islands

# soln = Solution()
# assert 1 == soln.numIslands([["1","1","1","1","0"],
# 							 ["1","1","0","1","0"],
# 							 ["1","1","0","0","0"],
# 							 ["0","0","0","0","0"]])

# assert 3 == soln.numIslands([["1","1","0","0","0"],
# 							 ["1","1","0","0","0"],
# 							 ["0","0","1","0","0"],
# 							 ["0","0","0","1","1"]])

# assert 1 == soln.numIslands([["1","0","1","1","1"],
# 							 ["1","0","1","0","1"],
# 							 ["1","1","1","0","1"]])