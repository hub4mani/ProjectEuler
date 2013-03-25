import os

f = open('./013.in', 'r')
sum = 0
for line in f:
  print line,
  sum = sum + int(line)
print "sum = ",sum,
