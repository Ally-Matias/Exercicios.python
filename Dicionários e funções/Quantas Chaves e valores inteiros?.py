import ast

frase = input("")

dic = ast.literal_eval(frase)
valores = list(dic.values())
chaves = list(dic.keys())

def funcao(chaves, valores):
	contc = 0
	contv = 0
	for c in chaves:
		if c == str(c):
			pass
		elif c == int(c):
			contc += 1
	for v in valores:
		if v == str(v):
			pass
		elif v == int(v):
			contv += 1
	return(contc, contv)

resposta = funcao(chaves, valores)
print(resposta)
