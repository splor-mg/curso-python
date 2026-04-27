# Classes
# métodos = comportamento
# atributos = dados 
class Aluno:
    def aprovar(self):
        print("Aprovado")
    
    def reprovado(self):
        print("Reprovado")

aluno1 = Aluno()
aluno2 = Aluno()
aluno1.nome = "Maria"
aluno2.idade = 10

print(aluno2.idade)
aluno1.aprovar()
