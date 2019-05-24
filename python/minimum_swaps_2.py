#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PROGRAMMER:       Daniel Rines
# DATE CREATED:     2019.05.23
# REVISED DATE:     2019.05.24
# PURPOSE:  Performs an integer sort on an array and outputs the
#           number of swaps it took to complete the sort.
#
# NOTES:    Uses a sort algorithm to sort the array.
#           Sort logic: 
#           1. start at the beginning.
#           2. check the value against the index value.
#           3. if it doesn't belong, swap the value with whatever is in
#              the spot where it belongs.
#           4. check the number in this place and repeat swap until the
#              the index position contains the correct value.
#
#           INPUT: arr: an array of integers
#           OUTPUT: minimum number of swaps to achieve sorted arr.
#
#   Example call:
#      python minimum_swaps_2.py
##

# I put a sample unsorted array here, so it runs easy, but this can be 
# converted to take in an array argument instead.

arr = [4, 3, 1, 2, 5, 10, 9, 6, 7, 8]
n = len(arr)

if n > 1:
    # track the no. of swaps it took, if any
    swap_count = 0

    # track the array position pointer
    i = 0
    while i < n:
        # compare the index position of the unsorted to the index value
        if arr[i] != i+1:
            # place the current value in a temporary holder
            a = arr[i]
            # update the current position with the min
            arr[i] = arr[a-1]
            # replace the min position with the temp
            arr[a-1] = a
            # increment the swap counter
            swap_count += 1
        else:
            # do not move the counter until this position is correct
            i += 1

    print(swap_count)
else:
    print(0)
