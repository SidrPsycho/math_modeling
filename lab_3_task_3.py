import numpy as np
from lab_3_task_1 import uskoreniye_svobodnogo_padeniya as g

xo = int(input('Введите начальное координаты х: '))
yo = int(input('Введите начальное значение у: '))
vo = int(input('введите начальное значение скорости: '))

a = np.zeros((6, 3))
a[1, 0] = 1
a[2, 0] = 2
a[3, 0] = 3
a[4, 0] = 4
a[5, 0] = 5

for x in a[:, 1]:
  x = xo + vo * a[:, 0]
  a[:, 1] = x

for y in a[:, 2]:
  y = yo + vo * a[:, 0] - ((g * (a[:, 0]**2))/2)
  a[:, 2] = y
print(a)
