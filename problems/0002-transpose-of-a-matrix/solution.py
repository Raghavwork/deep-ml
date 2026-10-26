def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    x = len(a)
    if x == 0:
        return []
    y = len(a[0])
    if y == 0:
        return []
    ans = []
    for col in range(y):
        temp = []
        for row in range(x):
            temp.append(a[row][col])
        ans.append(temp)
    
    return ans