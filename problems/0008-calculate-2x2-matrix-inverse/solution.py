import numpy as np
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    if matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1] == 0:
        return None
    return np.linalg.inv(matrix)