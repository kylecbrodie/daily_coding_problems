from random import randint

import matplotlib.pyplot as plt
import numpy as np

class Solution:
	def rand5(self):
		r7 = randint(1, 7)
		while r7 > 5:
			r7 = randint(1, 7)
		return r7

soln = Solution()

randint_sample = np.array([randint(1, 5) for i in range(10_000)])
rand5_sample = np.array([soln.rand5() for i in range(10_000)])

hist1 = np.hstack(randint_sample)
plt.hist(hist1, bins='auto')
plt.title("randint(1, 5) histogram")
plt.show()

hist2 = np.hstack(rand5_sample)
plt.hist(hist2, bins='auto')
plt.title("soln.rand5() histogram")
plt.show()