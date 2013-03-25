for num in reversed(range(100,999)):
  reversed_num = int(str(num)[::-1])
  pal_num = num*1000+reversed_num

  for div in reversed(range(100,999)):
    if pal_num%div == 0:
      print pal_num, "[", div, ",", pal_num/div, "]"
      break

