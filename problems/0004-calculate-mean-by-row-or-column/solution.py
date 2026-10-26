def findMean(sublist: list[float]) -> float:
	return sum(sublist)/len(sublist)

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means: list[float] = list()
	if mode == "row":
		for sublist in matrix:
			means.append(findMean(sublist))
	else:
		for i in range(len(matrix[0])):
			temp = []
			for j in range(len(matrix)):
				temp.append(matrix[j][i])
			means.append(findMean(temp))	
	return means