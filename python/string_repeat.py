s = 'aba'
n = 1000000000000

a_count = 0
l = len(s)

a_count = s.count('a') * (n // l)
a_count += s[:n % l].count('a')

print(a_count)