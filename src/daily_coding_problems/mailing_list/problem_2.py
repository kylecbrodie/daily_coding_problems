import functools as ftools
import operator as ops

def product_of_all_except_one(list):
	product_of_all = ftools.reduce(ops.mul, list)
	return [product_of_all // a for a in list]
