# lista com os numeros sorteados (1..75)
# sortear um numero aleatorio da lista acima
# garantir que nao tenho numero repetido
# informar ao usuario o numero sorteado
import random

numeros = list(range(1,76)) # primeiro inclusive e o ultimo exclusive
sorteados = []

contador = 1
while numeros:
    sorteado = random.choice(numeros)
    sorteados.append(sorteado)
    print(f"{contador} - Número sorteado: {sorteado}")
    numeros.remove(sorteado)
    contador += 1

print("Sorteados original", sorteados)
sorteados.sort()
print("Sorteados ordenados", sorteados)