#!/usr/bin/env python3

from person import Person
from numba import njit
import matplotlib.pyplot as plt
import matplotlib.pyplot
matplotlib.use("Agg")
from time import perf_counter as pc

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))

@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return(fib_numba(n-1) + fib_numba(n-2))

def main():
	f = Person(10)
	print(f.getAge())
	print(f.getDecades())
	print(f.fib())

	f.setAge(11)
	print(f.getAge())
	print(f.getDecades())
	print(f.fib())
	'''
	time = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
	fib_reg = []
	fib_speed = []
	fib_cpp = []
	for i in time:
		start = pc()
		fib_py(i)
		end = pc()
		fib_reg.append(round(end-start, 2))

		start = pc()
		fib_numba(i)
		end = pc()
		fib_speed.append(round(end-start, 2))

		f = Person(i)
		start = pc()
		f.fib()
		end = pc()
		fib_cpp.append(round(end-start, 2))

	plt.plot(time, fib_reg, 'ro')
	plt.plot(time, fib_speed, 'bo')
	plt.plot(time, fib_cpp, 'go')

	plt.savefig('30_45_fib.png')
	'''
	#print(Person(47).fib())   #-1323752223
	#print(fib_numba(47))	  # 2971215073

if __name__ == '__main__':
	main()

