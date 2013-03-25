for a in range(1,1000):
  for b in range(a+1, 1000):
    if a*a+b*b == (1000-a-b)**2:
        print "a = ", a
        print "b = ", b
        print "c = ", (1000-a-b)
        print "abc = ", a*b*(1000-a-b)
        break;
