
#!/usr/bin/python3

"""
module to rotate a 2D matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a given 2D matrix 90 degrees clockwise.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to complete the rotation
    for row in matrix:
        row.reverse()
