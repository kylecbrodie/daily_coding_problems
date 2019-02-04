class LRUCache:
	def __init__(self, capacity: int):
		"""
		:type capacity: int
		"""
		self.capacity = capacity
		self.cache = {}
		self.lru_queue = []

	def get(self, key: int) -> int:
		"""
		:type key: int
		:rtype: int
		"""
		try:
			value = self.cache[key] 
			self.lru_queue.remove(key)
			self.lru_queue.append(key)
			return value
		except KeyError:
			return -1

	def _evict_lru(self) -> None:
		lru_key = self.lru_queue.pop(0)
		del self.cache[lru_key]

	def put(self, key: int, value: int) -> None:
		"""
		:type key: int
		:type value: int
		:rtype: void
		"""
		self.cache[key] = value
		try:
			self.lru_queue.remove(key)
		except ValueError:
			pass
		self.lru_queue.append(key)
		if len(self.lru_queue) > self.capacity:
			self._evict_lru()