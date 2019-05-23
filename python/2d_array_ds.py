#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PROGRAMMER:       Daniel Rines
# DATE CREATED:     2019.05.23
# REVISED DATE:     2019.05.23
# PURPOSE:  Should return an integer, the maximum hourglass sum in the array.
#
# NOTES:    None
#
#   Example call:
#      python 2d_array_ds.py
##

arr = [[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]]

rows = len(arr)
cols = len(arr[0])
glass_sums = []
for row_idx in range(1, rows-1):
    for col_idx in range(1, cols-1):
        glass_sum = sum(arr[row_idx - 1][col_idx-1:col_idx+2])
        glass_sum += arr[row_idx][col_idx]
        glass_sum += sum(arr[row_idx + 1][col_idx-1:col_idx+2])
        print("row: {}, col: {}, sum: {}".format(row_idx, col_idx, glass_sum))
        glass_sums.append(glass_sum)

print(glass_sums)
print(max(glass_sums))
