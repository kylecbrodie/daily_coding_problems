class TwoStackQueue:
	def __init__(self):
		self._enqueue_stack = []
		self._dequeue_stack = []
	def enqueue(self, obj):
		self._enqueue_stack.append(obj)
	def dequeue(self):
		try:
			return self._dequeue_stack.pop()
		except IndexError:
			self._refill_dequeue_stack()
			return self._dequeue_stack.pop()
	def _refill_dequeue_stack(self):
		for _ in range(len(self._enqueue_stack)):
			self._dequeue_stack.append(self._enqueue_stack.pop())
	
queue1 = TwoStackQueue()
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
assert 1 == queue1.dequeue()
