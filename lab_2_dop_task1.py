a = (float(input('Первый коэф: ')))
b = (float(input('Второй коэф: ')))
c = (float(input('Третий коэф: ')))

D = (b**2) - (4 * a * c)

if D > 0:
  x1 = (-b - (D**0.5)) / (2 * a)
  x2 = (-b + (D**0.5)) / (2 * a)
  print('x1 = ' + str(x1))
  print('x2 = ' + str(x2))
elif D == 0:
  x = -b / (2*a)
  print('x = ' + str(x))
else:
  print('Корней нет')