def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	return [[val*scalar for val in sublist] for sublist in matrix ]