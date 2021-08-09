#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def find_subarray_with_max_sum(input_array):
    if not isinstance(input_array, list) or len(input_array) == 0:
        exit()

    result_list = list()

    for i in range(len(input_array)-1):
        max_sum = -sys.maxsize
        indexes = tuple()
        for j in range(i+1, len(input_array)):
            local_sum = sum(input_array[i:j+1])
            if local_sum > max_sum:
                max_sum = local_sum
                indexes = (i, j)
            else:
                break
            print('{}; {}'.format(i, j))
        print('max_sum = {}'.format(max_sum))
        result_list.append({indexes: max_sum})
    print('result = {}'.format(result_list))
    return tuple()



if __name__ == '__main__':
    find_subarray_with_max_sum([10, -3, -12, 8, 42, 1, -7, 0, 3])
    # cases = [
    #     ([10, -3, -12, 8, 42, 1, -7, 0, 3], (3, 5)),
    #     #([1, 2, 3, 4, 5], (1, 2)),
    #     #([-5, -4, -3, -2, -1], (1, 2)),
    # ]
    #
    # for array, expected_result in cases:
    #     assert findSubarrayWithMaxSum(array) == expected_result
