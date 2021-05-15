def anagrams(work,works):

	work = list(work)
	so= []
	for i in range(0,len(works)):
		if len(works[i]) == len(work):
			so.append(works[i])
	sol=[]
	sol2=[] 
	for i in range(0,len(work)):
		if work.count(work[i])==works[i].count(work[i]):
			sol.append(works[i])

	for i in so:
		x = False
		for j in range(0,len(work)):
			if i[j] not in work:
				x = True
			elif work[j] not in i:
				x = True
		if x == False:
			sol2.append(i)
	print(sol2)
	return sol2


#def anagrams(word, words): return print([item for item in words if sorted(item)==sorted(word)])
def anagrams(word, words):
	a =[]
	for item in words:
		if sorted(item)==sorted(word):
			a.append(item)
	return print(a)

	
anagrams('abba', ['a', 'b', 'c', 'd', 'aabb', 'bbaa', 'abab', 'baba', 'baab', 'abcd', 'abbba', 'baaab', 'abbab', 'abbaa', 'babaa'])
