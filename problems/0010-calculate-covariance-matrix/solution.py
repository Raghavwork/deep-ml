def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	if not vectors or not vectors[0]:
		return []
	
	n = len(vectors)
	m = len(vectors[0])

	ans = [[0.0 for j in range(n)] for i in range(n)]

	mean = [0.0 for i in range(n)]
	for i in range(n):
		smm = 0
		for j in range(m):
			smm += vectors[i][j]
		mean[i] = smm/m


	for i in range(n):
		for j in range(i,n):
			smm = 0.0
			for k in range(m):
				smm += (vectors[i][k] - mean[i])* (vectors[j][k] - mean[j])
			val = smm/(m-1)
			ans[i][j] = val
			ans[j][i] = val
	
	return ans