cons_set = set() 
LIMIT = 100001
prime_list = set([2])

for num in range(3,LIMIT,2):
  if num not in cons_set:
    prime_list.add(num)
    if len(prime_list) == 10001:
      print num
      break;
    for cons in range(num*2, LIMIT, num):
      cons_set.add(cons)

print len(prime_list)

ans = {(1,41):40}
large = 40
large_tup = (1,41)
for b in prime_list:
  if b<1000:
    for a in range(0,1001):
      print a,b
      count = 1
      if (a,b) not in ans:
        n=1
        while n*n + a*n + b in prime_list:
          count = count + 1
          n = n+1
        ans[(a,b)] = count
        if count > large:
          print count
          large = count
          large_tup = (a,b)
          print a,b

      count = 1
      b = b*-1
      if (a,b) not in ans:
        n=1
        while n*n + a*n + b in prime_list:
          count = count + 1
          n = n+1
        ans[(a,b)] = count
        if count > large:
          print count
          large = count
          large_tup = (a,b)
          print a,b

      count = 1
      a = a*-1
      if (a,b) not in ans:
        n=1
        while n*n + a*n + b in prime_list:
          count = count + 1
          n = n+1
        ans[(a,b)] = count
        if count > large:
          print count
          large = count
          large_tup = (a,b)
          print a,b

      count = 1
      b = b*-1
      if (a,b) not in ans:
        n=1
        while n*n + a*n + b in prime_list:
          count = count + 1
          n = n+1
        ans[(a,b)] = count
        if count > large:
          print count
          large = count
          large_tup = (a,b)
          print a,b
print large_tup,large

