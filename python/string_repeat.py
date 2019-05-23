#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PROGRAMMER:       Daniel Rines
# DATE CREATED:     2019.05.23
# REVISED DATE:     2019.05.23
# PURPOSE:  String manipulation without causing Memory Error.
#
# NOTES:    hackerrank: 
#
#   Example call:
#      python string_repeat.py
##

s = 'aba'
n = 1000000000000

a_count = 0
l = len(s)

a_count = s.count('a') * (n // l)
a_count += s[:n % l].count('a')

print(a_count)