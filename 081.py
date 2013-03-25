import os
import csv

def short_sum(matrix,DEPTH,WIDTH,i,j):
  if j==WIDTH-1 and i<DEPTH-1:
    return int(matrix[i][j]) + short_sum(matrix,DEPTH,WIDTH,i+1,j)
  
  if j<WIDTH-1 and i==DEPTH-1:
    return int(matrix[i][j]) + short_sum(matrix,DEPTH,WIDTH,i,j+1)

  if j==WIDTH-1 and i==DEPTH-1:
    return int(matrix[i][j])
  
  if j<WIDTH-1 and i<DEPTH-1:
    return int(matrix[i][j]) + min(short_sum(matrix,DEPTH,WIDTH,i,j+1),short_sum(matrix,DEPTH,WIDTH,i+1,j))

matrix = []
with open('./081_matrix.txt', 'r') as f:
  for line in csv.reader(f):
    matrix.append(line)

DEPTH = len(matrix)
WIDTH = len(matrix[0])
print WIDTH,DEPTH

print short_sum(matrix,DEPTH,WIDTH,0,0)

