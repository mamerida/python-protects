def to_camel_case(string):
	if string== []:
		return print("")
	string = string.replace(" ","-")
	string = string.replace("_","-")
	s = string.split("-")
	x=[s[0]]
	for i in range(1,len(s)):	
		x.append(s[i].capitalize())
	x = "".join(x)
	print(x)
	return x
to_camel_case('the_stealth_warrior')


"""
def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s
"""