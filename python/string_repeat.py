#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PROGRAMMER:       Daniel Rines
# DATE CREATED:     2019.05.23
# REVISED DATE:     2019.05.23
# PURPOSE:  String manipulation without causing Memory Error.
#
# NOTES:    Large repeat values will swamp memory if making
#           a replicate string; thus, need to be clever and 
#           perform calculation without making a long string.
#
#   Example call:
#      python string_repeat.py
##

s = 'aba'
n = 1000000000000

# counter to track 'a' occurrances
a_count = 0
l = len(s)

# multiply number of 'a's by final string length
# don't foget the extra values if partial replicate
# is within the length
a_count = s.count('a') * (n // l)
a_count += s[:n % l].count('a')

print(a_count)