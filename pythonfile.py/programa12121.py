def count_num(n):
  count = 0
  while n != 0:
      n //= n
      count +=1
  print(count)
count_num(384)