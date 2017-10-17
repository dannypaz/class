import numpy as np
import timeit

'''
Here are two solutions to the problem. The first is slow, but uses the matrix setup similar to the knapsack and longest common subsequence problems. It runs in O(n^2) time complexity. The other solution runs in O(n) but can be somewhat confusing to read at first. Although it is less lines of code, it is a bit slower. The fastest is the third method, which is the one Professor Bowles outlined in class.  
'''



def largestSumSubarray_matrix(arr):
	M = np.full((len(arr),len(arr)),-np.inf)
	for i,val1 in enumerate(arr):
		for j,val2 in enumerate(arr[i:]):
			M[i][j + i] = sum(arr[i:j + i + 1])
	index =  np.unravel_index(M.argmax(),M.shape)
	return arr[index[0]:index[1] + 1]

def largestSumSubarray_array(arr):
	M = [(0,0) for x in range(len(arr))]
	for i,A in enumerate(arr):
		M[i] = max((A,i),(M[i - 1][0] + A,M[i - 1][1]),key = lambda x: x[0])
	return arr[max(M,key = lambda x: x[0])[1]:M.index(max(M,key = lambda x: x[0])) + 1]

def largestSumSubarray_array_variable(arr):
	M = [arr[0]]
	idx = 0
	for i,val in enumerate(arr[1:]):
		M.append(max(val,M[i] + val))
		if val > M[i] + val:
			idx = i + 1
	return arr[idx:np.argmax(M) + 1]


if __name__ == '__main__':
	arrs = [1, -2, 3, 10, -4, 7, 2, -5]
	#arrs = [-1,-2,-3,-100]
	print largestSumSubarray_matrix(arrs)
	print timeit.timeit('largestSumSubarray_matrix([1, -2, 3, 10, -4, 7, 2, -5])',setup="from __main__ import largestSumSubarray_matrix",number = 10000)
	print largestSumSubarray_array(arrs)
	print timeit.timeit('largestSumSubarray_array([1, -2, 3, 10, -4, 7, 2, -5])',setup="from __main__ import largestSumSubarray_array",number = 10000)
	print largestSumSubarray_array_variable(arrs)
	print timeit.timeit('largestSumSubarray_array_variable([1, -2, 3, 10, -4, 7, 2, -5])',setup="from __main__ import largestSumSubarray_array_variable",number = 10000)

