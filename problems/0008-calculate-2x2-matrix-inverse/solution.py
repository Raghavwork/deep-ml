def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    val = a*d - b*c
    if val == 0:
        return None
    
    ans: list[list[float]] = [[0.0 for j in range(2)] for i in range(2)]
    ans[0][0] = d / val
    ans[0][1] = (-1*b) / val
    ans[1][0] = (-1*c) / val
    ans[1][1] = a / val
    return ans