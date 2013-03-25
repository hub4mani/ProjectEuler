count = 0
for n in range(19,10000):
  n_str = str(n)
  LIMIT = 53 
  while LIMIT:
    # print n_str
    LIMIT -= 1
    n_str = str(int(n_str) + int( str(n_str)[::-1] ))
    length = len(n_str)

    # print n_str[:length/2] , n_str[:length/2-(length+1)%2:-1]
    if n_str[:length/2] == n_str[:length/2-(length+1)%2:-1]:
      break
  if LIMIT == 0:
    print n
    count += 1

print "count = ", count

