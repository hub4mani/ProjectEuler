count_list = [
    3*191, #one
    3*190,
    4*190,
    4*190,
    3*190,
    5*190,
    5*190,
    4*190, #nine
    3*10,  #ten
    6*10,
    6*10,
    8*10,
    8*10,
    7*10,
    7*10,
    9*10,
    8*10,
    8*10, #nineteen
    6*100, #twenty
    6*100, #thirty
    5*100, #forty
    5*100, #fifty
    5*100, #sixty
    7*100, #seventy
    6*100, #eighty
    6*100, #ninety
    7*900,#hundred
    8,    # thousand
    3*99*9 #and
    ]

sum = 0
for num in count_list:
  sum = sum + num
print sum
