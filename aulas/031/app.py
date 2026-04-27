class Aluno:
    def __init__(self, nome, idade, escola="escola1"):
        self.nome = nome
        self.idade = idade
        self.escola = escola

    def aprovar(self):
        print("Aprovado")
    
    def reprovado(self):
        print("Reprovado")

aluno1 = Aluno("Ana", 14)
aluno1.idade = 15
print(aluno1.nome)
print(aluno1.idade)
print(aluno1.escola)

