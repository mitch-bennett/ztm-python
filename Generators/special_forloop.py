def special_for(iterable):
  iterator = iter(iterable)
  while True:
    try:
      iterator*5
      next(iterator)
    except StopIteration:
      break

special_for([1,2,3,4,5])