some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

dup = []
another_list = []
for item in some_list:
  if item not in another_list:
    another_list.append(item)
  else:
    dup.append(item)
print(dup)