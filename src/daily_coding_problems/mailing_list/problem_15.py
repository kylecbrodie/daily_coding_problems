class Solution:
	def pickElemOfStreamWithUniformProb(self):
		"""
		Hash functions usually have the property that their outputs are
		uniformly distributed. Since we don't know the length of our input
		stream and the elements are too large to store in memory, we hash a
		running index of the elements (first element has index 0 then 1) and
		if it falls within a range of hashes we return the current element.
		The range of hashes is derived from a uniform random number [0, 1)
		that is selected before processing the input stream. The more
		significant digits in the random number the narrower the range of
		hashes. If the hash function outputs a 32-bit value then a random
		number of 0.978 corresponds to the 32-bit values that are between
		97.8% (inclusive) and 97.9% (not-inclusive) of the way between 0
		and 2^32. Put another way, the start of the range is floor(r*2^32)
		and the end of the range is start + floor(10^(-d_r)*2^32) where r is
		the random number selected and d_r is the number of significant digits
		of r after the decimal point. So for 0.978 again the start is
		floor(0.978*2^32) = 4,200,478,015 and the end is
		start + floor(10^(-3)*2^32) = 4,200,478,015 + 4,294,967 = 4,204,772,982.
		"""
