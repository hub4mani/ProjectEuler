map = {}
large = 1
trig_n = 1

for n in range(7, 100):
  count =2;
  trig_number = n*(n+1)/2
  print trig_number, " -> ",
  for div in range(2,trig_number/2+1):
    if trig_number%div == 0:
      print div,
      count = count + 1
  map[trig_number] = count
  print

  if count > large:
    large = count
    trig_n = trig_number

  if count == 500:
    print tring_number, "->", count
    break

print trig_n,large 
