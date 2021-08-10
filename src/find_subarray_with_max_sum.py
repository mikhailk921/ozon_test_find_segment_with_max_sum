#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def find_subarray_with_max_sum(input_array):
    """
    The function searches the indices of the begin and end of the subarray with the maximum sum.

    Parameters:
        input_array (list): Input array of numbers.

    Returns:
        indices(tuple): Tuple with the desired subarray indices.
    """
    if not isinstance(input_array, list) or len(input_array) < 2:
        exit(-1)

    results = dict()
    for i in range(len(input_array)-1):
        max_sum = -sys.maxsize
        indexes = (-1, -1)
        for j in range(i+1, len(input_array)):
            local_sum = sum(input_array[i:j+1])
            if local_sum > max_sum:
                max_sum = local_sum
                indexes = (i, j)
        results[max_sum] = indexes
    return list(dict(sorted(results.items(), reverse=True)).values())[0]


if __name__ == '__main__':

    cases = [
        ([10, -3, -12, 8, 42, 1, -7, 0, 3], (3, 5)),
        ([1, 2, 3, 4, 5], (0, 4)),
        ([-5, -4, -3, -2, -1], (3, 4)),
        ([-5, 100, -59, 24, -5, 16, 78, -86, 98, -34], (1, 8)),
        ([10, -3, -12, 50, -42, 1, -7, 0, 3], (0, 3)),
    ]

    for array, expected_result in cases:
        assert find_subarray_with_max_sum(array) == expected_result
