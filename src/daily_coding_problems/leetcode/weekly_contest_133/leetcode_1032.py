from typing import List
from collections import deque
from bisect import insort_left

class StreamChecker:
	def __init__(self, words: List[str]):
		max_word_length = 0
		self.word_by_ending_letter = {}
		for word in words:
			max_word_length = max(max_word_length, len(word))
			ending_letter = word[-1]
			try:
				insort_left(self.word_by_ending_letter[ending_letter], word)
			except KeyError:
				self.word_by_ending_letter[ending_letter] = [word]
		self.character_deque = deque(maxlen=max_word_length)
		

	def query(self, letter: str) -> bool:
		self.character_deque.append(letter)
		try:
			words_ending_in_letter = self.word_by_ending_letter[letter]
		except KeyError:
			pass
		else:
			for word in words_ending_in_letter:
				if len(word) <= len(self.character_deque):
					i = len(word) - 1
					for letter in reversed(self.character_deque):
						if letter != word[i]:
							break
						i -= 1
						if i < 0:
							return True
		return False

streamChecker = StreamChecker(["cd","f","kl"])
streamChecker.query('a')
streamChecker.query('b')
streamChecker.query('c')
assert streamChecker.query('d')
streamChecker.query('e')
assert streamChecker.query('f')
streamChecker.query('g')
streamChecker.query('h')
streamChecker.query('i')
streamChecker.query('j')
streamChecker.query('k')
assert streamChecker.query('l')
