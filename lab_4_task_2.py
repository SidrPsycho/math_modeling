def func(*args):
  i = 0
  s = 1
  while i < len(args):
    s = s * args[i]
    i = i + 1
  print(s)

func(2, 3, 4, 134)