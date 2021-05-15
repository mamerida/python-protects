def dirReduc(arr):
    dict = {"NORTH":"SOUTH","SOUTH":"NORTH","EAST":"WEST","WEST":"EAST"}
    res = []
    for i in arr:
    	if res and dict[i] == res[-1]:
    		res.pop()
    	else:
    		print("soy el rest del else " ,res)
    		res.append(i)
    print(res)
    return res


u = ["NORTH", "SOUTH", "EAST", "WEST"]
dirReduc(u)


		
