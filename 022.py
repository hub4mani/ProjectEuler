import os

f = open('./022_sorted.txt', 'r')
sum = 0
alpha_val = { 'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26 }

line_num = 1
for line in f:
  rank = 0
  for char in line.rstrip('\n'):
    rank = rank + alpha_val[char]
  sum = sum + (rank * line_num)
  line_num = line_num + 1

print "sum = ",sum,
