def recursive_fact(x):
  if(x==0):
    return 1
  else:
    fact=x*(recursive_fact(x-1))
    return fact
  
a=recursive_fact(3)
print(a)
