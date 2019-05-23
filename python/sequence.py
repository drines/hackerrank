n = 10

p_value = 0
count = 1
while count <= n:
    p_value += 10**(n-count) * count
    count += 1

print(p_value)
