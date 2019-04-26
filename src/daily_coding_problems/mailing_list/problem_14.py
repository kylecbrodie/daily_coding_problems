import numpy as np
import numpy.random as np_random

class Solution:
	def monteCarloPiEstimate(self, num_samples=1_000_000):
		"""
		We can estimate pi by randomly picking points in the square
		(0, 0) <= (x, y) <= (1, 1)
		and computing their distance. If their distance is <= 1 then they are
		inside the unit circle. The ratio of the number of points inside the
		unit circle to the number of points picked approximates the ratio of
		the quarter circle and square areas, (pi / 4) : 1. Multiplying the ratio
		by 4 yields an estimate for pi. Ensuring 3 decimal places of accuracy,
		requires at least 1,000,000 points as error is preportional to
		1/(sqrt(num_points))
		"""
		x_samples = np_random.sample(num_samples)
		y_samples = np_random.sample(num_samples)
		samples_within_unit_circle = (x_samples**2 + y_samples**2) <= 1
		return round(
			4 * np.count_nonzero(samples_within_unit_circle) / num_samples, 3
		)

soln = Solution()
print(soln.monteCarloPiEstimate())
print(soln.monteCarloPiEstimate())
print(soln.monteCarloPiEstimate())
print(soln.monteCarloPiEstimate())
print(soln.monteCarloPiEstimate())
