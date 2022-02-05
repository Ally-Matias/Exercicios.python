elem = [int(x) for x in input("").split()]

def formula(a1, r, n):
	return a1 + (n - 1) * r
	
resposta = formula(elem[0], elem[1], elem[2])

def soma(a1, en, n):
	return ((a1 + en) * n) / 2
		
resp  = soma(elem[0], resposta, elem[2])

print("{} {} {:.2f}".format(elem[0], resposta, resp))

