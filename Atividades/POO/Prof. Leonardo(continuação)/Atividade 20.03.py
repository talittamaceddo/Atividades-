# Programa para exibir de 1 até 10
for i in range (1, 11):
   print(i)


# Peça ao usuário p/ dar o comando do print.


a = int(input("Você quer ver os números de 1 a 10? Se sim. digite 1 e se não, digite 2: "))
num = a
if num == 1:
   for i in range(1,11):
    print(i)
else:
   print("Aguardando sua boa vontade...")


# Se o usuário não quiser receber os números de 1 até 10, peça um número ao usuário e printe a sequência de números até o valor informado.


a = int(input("Você quer ver os números de 1 a 10? Se sim. digite 1 e se não, digite 2: "))
num = a
if num == 1:
   for i in range(1,11):
    print(i)
elif num == 2:
   b = int(input("Não quer ver os 10 números? Digite o número (1 a 10) que você quer que a lista vá: "))
   for i in range(1, b + 1):
    print(i)


# Faça seu programa continuar rodando enquanto o usuário não der um comando de parada:

parada = False
while parada == False:
   a = int(input("Você quer ver os números de 1 a 10? Se sim. digite 1, se não, digite 2 e se quiser parar o programa digite 3: "))
if a == "1":
   for i in range(1,11):
    print(i)
elif a == "2":
    try:
        b = int(input("Não quer ver os 10 números? Digite o número (1 a 10) que você quer que a lista vá: "))
        for i in range(1, b + 1):
            print(i)
    except ValueError:
        print("O número é inválido. Esperando uma nova tentativa...")
elif a == "3":
    parada = True