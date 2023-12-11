b=[1, 6, 1, 7, 8, 9, 1, 5, 7, 8]

for i in range(len(b)):
  if i >= len(b):
    break
  if b.count(b[i]) > 1:
     b.pop(i)
print(b, ' изменённый массив')

