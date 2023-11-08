#!/usr/bin/python3
"""Defines a pascal triangle."""


def pascal_triangle(n):
    """This function creates a pascal triangle of a given number n.

    Args:
        n (int): The given number representing the size.

    Return:
        A list of integers representing the Pascal's triangle of n.
    """

    if n <= 0:
        return []

    triangle = []

    row = [1]

    for _ in range(n):
        next_row = [1]

        for i in range(1, len(row)):
            next_row.append(row[i] + row[i - 1])

        next_row.append(1)

        triangle.append(row)
        row = next_row

    return triangle
