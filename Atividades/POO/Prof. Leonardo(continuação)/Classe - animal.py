class Animal:
    def __init__(self, nome, idade, especie, peso, altura):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.peso = peso
        self.altura = altura

    def emitir_som(self):
        print(f'{self.nome} está emitindo som.')
    def mover(self):
        print(f'{self.nome} está se movimentando.')
    def comer(self):
        print(f'{self.nome} está comendo.')
    def dormir(self):
        print(f'{self.nome} está dormindo.')

class Passaro(Animal):
    def __init__(self, nome, idade, especie, peso, altura, cor):
        super().__init__(nome, idade, especie, peso, altura)
        self.cor = cor
    def mover(self):
        print(f'{self.nome} está voando.')
    def emitir_som(self):
        print(f'{self.nome} está piando.')
    def comer(self):
        print(f'{self.nome} está bicando.')
    def dormir(self):
        print(f'{self.nome} está dormindo no ninho.')

animal_generico = Animal("bichano", 3, "genérico", 10, 0.5)
passaro_exemplo = Passaro(nome="Canarinho", idade=3, especie="Serinus canaria", peso=0.02, altura=0.1, cor="Amarelo")
passaro_exemplo.emitir_som()
passaro_exemplo.mover()
passaro_exemplo.comer()
passaro_exemplo.dormir()
print(f"\nCor do pássaro: {passaro_exemplo.cor}")
