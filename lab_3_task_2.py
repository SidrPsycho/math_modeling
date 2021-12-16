import numpy as np
from lab_3_task_1 import uskoreniye_svobodnogo_padeniya as g
from lab_3_task_1 import postoyannaya_Bolcmana as k
from lab_3_task_1 import chislo_Eylera as e
from lab_3_task_1 import postoyannaya_Planka as ℏ

h = 100
a = np.pi/3
b = 30
T = 200
ε = 300

x = np.sqrt(((g * h) * (np.tan(b))**2) / 2 * (np.cos(a))**2 *(1 - (np.tan(b) * np.tan(a))))
print('%.2f' % x)

y = (2 / np.pi) * (ℏ / ((k * T)**(3/2))) * e**(-ε / (k * T)) * ε**(T/2)
print(y)