a = int(input('Введите натуральное число: ')) + 1
b = 1
c = 1
x = 0

while a != 0:
  b = c
  c = x
  x = b + c 
  a -= 1
  print(x)
  