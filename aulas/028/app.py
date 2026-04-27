try:
    idade = int(input("idade: "))
    salario = 10000
    risco = salario / idade 
    print(idade)
except ValueError:
    print("Idade inválida")
except ZeroDivisionError: 
    print("A idade não pode ser 0")