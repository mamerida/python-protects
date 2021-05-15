def tower_builder(n_floors):
	j = []
	j2 = []
	x ="*"
	for i in range (0,n_floors):
		j.append( x + x*(i*2)) 
	h = len(j[-1])
	for i in j:
		j2.append(i.center(h))

	print(j2)
	return j2
"""
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
"""

