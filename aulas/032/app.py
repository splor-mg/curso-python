class Animal:
    def passear(self):
        print("passear")


class Cachorro(Animal):
    def latir(self):
        print("au au")


class Gato(Animal):
    pass

caramelo1 = Cachorro()
caramelo1.passear()
caramelo1.latir()