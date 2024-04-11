class Pessoa:
   def __init__(self, nome, idade, altura, peso, genero):
       self.nome = nome
       self.idade = idade
       self.altura = altura
       self.peso = peso
       self.genero = genero
       self.comendo = False
       self.falando = False
       self.andando = False
       self.dormindo = False

   def comer(self, alimento):
       if self.falando:
           print(f'{self.nome} não pode comer enquanto fala.')
       if self.andando:
           print(f'{self.nome} está comendo e andando.')
       if self.dormindo:
           print(f'{self.nome} não pode comer enquanto está dormindo.')
       print(f'{self.nome} está comendo {alimento}.')
       self.comendo = True
   def parar_comer(self, alimento):
       if not self.comendo:
           print(f'{self.nome} não está comendo {alimento}.')
       print(f'{self.nome} parou de comer.')

   def falar(self, conteudo):
       if self.comendo:
           print(f'{self.nome} não pode falar enquanto come.')
       if self.dormindo:
           print(f'{self.nome} não pode falar enquanto dorme.')
           print(f'{self.nome} está falando.')
           self.falando = True #ativa o método falar
   def parar_falar(self):
       if not self.falando:
           print(f'{self.nome} não está falando.')
       print(f'{self.nome} parou de falar.')
       self.falando = False

   def andar(self, destino):
     if self.dormindo:
       print(f'{self.nome} não pode andar enquanto dorme.')
       if self.comendo:
           print(f'{self.nome} está andando e comendo.')
       if self.falando:
           print(f'{self.nome} está andando e falando')
       print(f'{self.nome} está indo para {destino}.')
       self.andando = True
   def parar_andar(self):
       if not self.andando:
           print(f'{self.nome} não está andando.')
       print(f'{self.andar} parou de andar.')
       self.andando = False

   def dormir(self, lugar):
       if self.falando:
           print(f'{self.nome} não pode falar enquanto dorme.')
       if self.comendo:
           print(f'{self.nome} não pode comer enquanto dorme.')
       if self.andando:
        print(f'{self.nome} não pode anadar enquanto dorme.')
       print(f'{self.nome} está dormindo em {lugar}.')
       self.dormindo = True
   def acordar(self):
       if not self.dormindo:
           print(f'{self.nome} não está dormindo.')
       print(f'{self.nome} acordou.')
       self.dormindo = False

Helena = Pessoa(nome='Helena', idade='29', altura='1.68', peso='60 kg', genero='feminino')
Helena.comer("maçã")
Helena.falar("Olá, como vai?")
Helena.comer("pão")
Helena.parar_falar()
Helena.dormir("cama")
Helena.andar("parque")
Helena.acordar()