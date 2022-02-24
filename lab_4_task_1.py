def func(*args):
  i = 0
  s = 0
  while i < len(args):
    s = s + args[i]
    i = i + 1
  print(s/len(args))

func(2, 3, 7, 11)