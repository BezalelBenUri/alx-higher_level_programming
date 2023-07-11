#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        trity = triangles[-1]
        tmpry = [1]
        for i in range(len(trity) - 1):
            tmpry.append(trity[i] + trity[i + 1])
        tmpry.append(1)
        triangles.append(tmpry)
    return triangles
