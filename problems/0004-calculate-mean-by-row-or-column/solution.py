def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means: list[float] = list()
	if not matrix or not matrix[0]:
		return []
	
	if mode == "row":
		return [sum(sublist)/len(matrix[0]) for sublist in matrix]
	else:
		n = len(matrix)
		m = len(matrix[0])

		return [sum(matrix[i][j] for i in range(n))/n for j in range(m)]
	
	raise ValueError("mode must be 'row' or 'column'")