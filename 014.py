large = 10
map = {}

for num in reversed(range(13, 1000000)):
  collatz_size = 1
  orig_num = num
  while num <> 1:
    if num%2 == 0:
      num = num/2
    else:
      num = 3*num+1
    collatz_size = collatz_size + 1

  map[orig_num] = collatz_size

  if collatz_size > large:
    large = collatz_size
    print "[", orig_num, ", ", collatz_size, "]"
print "result = ", large
