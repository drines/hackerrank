#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PROGRAMMER:       Daniel Rines
# DATE CREATED:     2019.05.23
# REVISED DATE:     2019.05.23
# PURPOSE:  Performs a left rotation on an array.
#
# NOTES:    
#           INPUT: length and left shift amount
#           OUTPUT: Modified (shifted) array
#
#   Example call:
#      python arrays_left_rotation.py
##

arr = [1, 2, 3, 4, 5]
d = 4           # desired shift number
n = len(arr)

U = d % n
shifted_arr = arr[U:]+arr[:U]
print(shifted_arr)
