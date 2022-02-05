import ast

frase = input("")
inp = input("").split( )

dic = ast.literal_eval(frase)

def funcao(dic):
	inteiro = 0
	strin = ""
	Float = 0
	if inp[1] == "int":
		inteiro = int(inp[0])
	elif inp[1] == "string":
		strin = inp[0]
	elif inp[1] == "float":
		Float = float(inp[0])
		
	lista = []
	for c, v in dic.items():
		if v == inteiro:
			lista.append(c)
		elif v == strin:
			lista.append(c)
		elif v == Float:
			lista.append(c)
	return lista

resposta = funcao(dic)
print(resposta)
