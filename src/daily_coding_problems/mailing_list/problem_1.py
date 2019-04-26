import operator as ops

def do_two_elems_sum_to_k(list, k):
	fast_lookup = set(list)
	try:
		return next(filter(ops.truth, ((k - a in fast_lookup) for a in list)))
	except StopIteration:
		return False
