lista = []
soma = 0
n = int(input(""))
media = 0
count = 1
soma = 0
i = 0

while count <= n:
    count += 1
    num = float(input(""))
    lista.append(num)
    soma += num

media = soma / n

while i < n:
    if lista[i] >= media:
        soma += 1
    i += 1
print("{:.0f}  {:.2f}".format(soma, media))
