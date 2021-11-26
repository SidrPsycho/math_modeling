a = int(input('Введите число: '))
b = len(str(a))
c = 0

while b != 0:
  c = (a % 10)
  a //= 10
  print(c, end=' ')
  b -= 1