elem = [int(x) for x in input("").split()]

def pertence(a1, r, n):
	if (n- a1) % r == 0:
		return ("1")
	else:
		return ("0")
		
resp = pertence(elem[0], elem[1], elem[2])

print(resp)
