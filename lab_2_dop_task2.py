a = int(input('Введите длину первого отрезка: '))
b = int(input('Введите длину второго отрезка: '))
c = int(input('Введите длину третьего отрезка: '))

if a + b > c or a + c > b or b + c > a:
  if a == b == c:
    print('Такой треугольник может быть, и он будет равносторонним!')
  elif a == b or a == c or b == c:
    print('Такой треугольник может быть, и он будет равнобедренным!')
  else:
    print('Такой треугольник может быть, и он будет разносторонним!')
else:
  print('Такого треугольника не может быть!')
