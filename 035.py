cons_set = set() 
LIMIT = 1000000
prime_list = set([2])

for num in range(3,LIMIT,2):
  if num not in cons_set:
    prime_list.add(num)

    for cons in range(num*2, LIMIT, num):
      cons_set.add(cons)

print len(prime_list)

circular_primes = set()
for p in prime_list:
  plist = [p]
  circular = True

  str_p = str(p)
  for i in range (1,len(str_p)):
    next_num = int(str_p[i:] + str_p[0:i])
    # print next_num,
    if next_num not in prime_list:
      circular = False
      break
    plist.append(next_num)
  if circular:
    for item in plist:
      circular_primes.add(item)
  #print

print len(circular_primes)
