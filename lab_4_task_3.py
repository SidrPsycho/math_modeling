g = 9.8
h = int(input('Высота = '))
m = int(input('Масса = '))
v = int(input('Скорость = '))
a = [g, h, m, v]

def E(a):
  x = m*g*h + ((m*(v**2))/2)
  return x

print(E(a))
