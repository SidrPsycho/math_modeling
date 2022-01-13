a = float(input('число а = '))
n = float(input('число n = ')) - 1
x = a

def st(a):
  global n
  global x
  while n != 0:
    x *= a
    n -= 1
    if n == 0:
      return x

print(st(a))