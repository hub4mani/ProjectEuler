num_str = str(2**1000)
print num_str

sum = 0
length = len(num_str)
for i in range(length):
  sum = sum + int(num_str[i])
print sum
