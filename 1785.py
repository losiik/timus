numb = int(input())

if numb <= 4:
  print("few")
elif numb <= 9:
  print("several")
elif numb <= 19:
  print("pack")
elif numb <= 49:
  print("lots")
elif numb <= 99:
  print("horde")
elif numb <= 249:
  print("throng")
elif numb <= 499:
  print("swarm")
elif numb <= 999:
  print("zounds")
else:
  print("legion")