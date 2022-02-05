n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
op = 0

while op != 5:
	print('''	[ 1 ] Somar
	[ 2 ] Multiplicar
	[ 3 ] Maior
	[ 4 ] Novos números
	[ 5 ] Sair do programa''')
	op = int(input(">>>Qual sua opção?: "))
	if op == 1:
		soma = n1 + n2
		print ("A soma entre {} e {} é {}".format (n1, n2, soma))
	elif op == 2:
		multi = n1 * n2
		print ("A multiplicação entre {} e {} é {}".format (n1, n2, multi))
	elif op == 3:
		if n1 > n2:
			print ("O maior número é {}".format (n1))
		elif n2 > n1:
			print ("O maior número é {}".format (n2))
		elif n1 == n2:
			print("São números iguais!")
	elif op == 4:
		print ('Informe os números novamente: ')
		n1 = int(input("Primeiro novo número: "))
		n2 = int(input("Segundo novo número: "))
	elif op == 5:
		print ("Finalizando...")
	else:
		print ("Opção invalida, tente novamente!")
print ("Fim do programa! :)")
