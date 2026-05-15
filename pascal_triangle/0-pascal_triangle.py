#!/usr/bin/python3
"""
Module that implements Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of n rows.

    Args:
        n (int): Number of rows in Pascal's triangle

    Returns:
        list: A list of lists of integers representing Pascal's triangle.
              Returns an empty list if n <= 0.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):

        row = [1] * (i + 1)


        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
