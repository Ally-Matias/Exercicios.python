chaves = input("").split( )
valores = input("").split( )

def funcao(dic):
	chaves = list(dic.keys())
	chaves.sort()
	for c in chaves:
		print("{}: {}".format(c, dic[c]))

dic = {}

for c in range (len(chaves)):
	dic[chaves[c]] = valores[c]
		
funcao(dic)
