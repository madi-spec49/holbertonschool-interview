#!/usr/bin/python3
"""Module for calculating minimum operations to reach n H characters."""


def minOperations(n):
    """Calculates the fewest number of operations needed to result in
    exactly n H characters.

    Args:
        n (int): The target number of H characters

    Returns:
        int: The minimum number of operations, or 0 if impossible
    """
    if not isinstance(n, int) or n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
