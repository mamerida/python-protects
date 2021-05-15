def bouncingBall(h, bounce, window):
	if bounce >=1 or h < window:
		return -1



	con = 0  
	s = h 

	while s > window :
		con = con + 1
		s = s * bounce
		if s > window:
			con = con +1 

	
	print(con)
	return con

"""
def bouncingBall(h, bounce, window):
    if not 0 < bounce < 1: return -1
    count = 0
    while h > window:
        count += 1
        h *= bounce
        if h > window: count += 1
    return count or -1
 """