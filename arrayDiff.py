#def array_diff(a, b):
#    return print([x for x in a if x not in b])
def array_diff(a, b):
    for i in b:
      if i in a:
        for j in range(a.count(i)):
          a.remove(i)
    return print(a)

array_diff([1,2,2],[1])