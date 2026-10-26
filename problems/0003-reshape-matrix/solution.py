import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	if not a:
		return []
	n = len(a)
	m = len(a[0])
	if m == 0 or new_shape == 0:
		return []

	if new_shape[0]*new_shape[1] != n*m:
		return []

	reshaped_matrix = []
	temp_matrix = []
	col = 0
	temp = np.concatenate(a).tolist()
	for val in temp:
		temp_matrix.append(val)
		col+=1
		if col == new_shape[1]:
			reshaped_matrix.append(temp_matrix)
			temp_matrix = []
			col = 0
	
	return reshaped_matrix