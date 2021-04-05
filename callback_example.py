#Callback
def f1():
  print('this is f1')
def f2():
  print('this is f2')
def f3():
  print('this is f3')
def outer(fn):
  fn()
outer(f1)
outer(f2)

