elem = [int(x) for x in input("").split()]

def formula(a1, r, n):
	return a1 + (n - 1) * r
	
resposta = formula(elem[0], elem[1], elem[2])

print(resposta)
