# 10001 th prime

cons_set = set() 
LIMIT = 10000001
prime_list = [2]

for num in range(3,LIMIT,2):
  if num not in cons_set:
    prime_list.append(num)
    if len(prime_list) == 10001:
      print num
      break;
    for cons in range(num*2, LIMIT, num):
      cons_set.add(cons)

print len(prime_list)
      
