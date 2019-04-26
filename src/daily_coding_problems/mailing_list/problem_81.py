# @lc app=leetcode id=17 lang=python3
from itertools import product
from string import ascii_lowercase
from typing import (
	List,
	Mapping,
)

# also LeetCode 17
class Solution:
	def __init__(self):
		self.phoneDigitLetterMap = {}
		prev_end = 0
		for i in range(2, 10):
			letters_start = prev_end
			prev_end = letters_end = letters_start + (
				3 if i != 7 and i != 9 else 4
			)
			letters = list(ascii_lowercase[letters_start:letters_end])
			self.phoneDigitLetterMap[str(i)] = letters

	def letterCombinations(self, digits: str) -> List[str]:
		return self.letterCombinationsMailingList(
			self.phoneDigitLetterMap, digits
		)

	def letterCombinationsMailingList(
		self, digits_to_letters: Mapping[str, List[str]], digits: str
	) -> List[str]:
		"""
		Daily Coding Problems 81
		A mapping of digits to letters is provided. LeetCode assumes phone mapping
		"""
		if len(digits) == 0:
			return []
		return list(
			map(
			lambda t: ''.join(t),
			product(*(digits_to_letters[digit] for digit in digits))
			)
		)
