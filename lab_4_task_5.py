import numpy as np

a = float(input('''Нажмите 1, чтобы найти пложадь круга
Нажмите 2, чтобы найти площадь прямоугольника
Нажмите 3, чтобы найти площадь треугольника  '''))

def ploshad(a):
  if a == 1:
    r = float(input('радиус = '))
    x = 2 * np.pi * r
    return x 
  elif a == 2:
     y = float(input('первая сторона = '))
     z = float(input('вторая сторона = '))
     x = y * z
     return x
  elif a == 3:
    y = float(input('основание = '))
    z = float(input('высота = '))
    x = (y * z) / 2
    return x
  else:
    x = 'ERROR'
    return(x)

print(ploshad(a))