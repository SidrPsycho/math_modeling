a = int(input('Введите первое число: '))
b = int(input('Введите знаменатель: '))
c = int(input('Введите кол-во членов: '))
print(a)

while c != 0:
  a *= b
  c-= 1
  print(a)