#!/usr/bin/python3
""" Rotates a 2D matrix """


def rotate_2d_matrix(matrix):
    """
       Rotates 2D matrix 90 degrees clockwise
       Matrix is edited in-place
       Args:
          matrix
    """
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            topLeft = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = topLeft

        right -= 1
        left += 1
