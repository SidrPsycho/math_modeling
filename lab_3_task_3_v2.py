import numpy as np
from lab_3_task_1 import uskoreniye_svobodnogo_padeniya as g

xo = int(input('Введите начальное координаты х: '))
yo = int(input('Введите начальное значение у: '))
vo = int(input('Введите начальное значение скорости: '))
N = int(input('интервал '))


a = np.zeros((N, 3))
a[0, 0] = 0

for i in a[:, 0]:
  i += 1
  a[:, 0] = i

for x in a[:, 1]:
  x = xo + vo * a[:, 0]
  a[:, 1] = x

for y in a[:, 2]:
  y = yo + vo * a[:, 0] - ((g * (a[:, 0]**2))/2)
  a[:, 2] = y
print(a)
