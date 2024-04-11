class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.limite = 0
        self.conta_ativa = False

    def sacar(self, valor):
        if self.conta_ativa and (self.saldo + self.limite >= valor):
            self.saldo -= valor
            print("Saque efetuado.")
        else:
            print("Saldo insuficiente ou conta bloqueada.")

    def depositar(self, valor):
        if self.conta_ativa:
            self.saldo += valor
            print("Depósito de", valor, "realizado com êxito.")
        else:
            print("A conta está bloqueada. Não é possível fazer depósitos.")

    def bloquear(self):
        self.conta_ativa = False
        print("Conta bloqueada.")

    def desbloquear(self):
        self.conta_ativa = True
        print("Conta desbloqueada.")

    def verificar_saldo(self):
        print("Saldo atual da sua conta:", self.saldo)

    def alterar_limite(self, novo_limite):
        if novo_limite >= 0:
            self.limite = novo_limite
            print("Limite alterado para", novo_limite)
        else:
            print("O limite deve ser um valor positivo.")


nome_titular = input("Digite o nome do titular da conta: ")
saldo_inicial = float(input("Digite o saldo inicial da conta: "))
conta = ContaBancaria(nome_titular, saldo_inicial)


while True:
    print("\nOpções:")
    print("1. Sacar")
    print("2. Depositar")
    print("3. Bloquear conta")
    print("4. Desbloquear conta")
    print("5. Verificar saldo")
    print("6. Alterar limite")
    print("0. Sair")

    opcao = input("Selecione uma opção do menu acima: ")

    if opcao == "1":
        valor_saque = float(input("Digite o valor que você deseja sacar: "))
        conta.sacar(valor_saque)
    elif opcao == "2":
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        conta.depositar(valor_deposito)
    elif opcao == "3":
        conta.bloquear()
    elif opcao == "4":
        conta.desbloquear()
    elif opcao == "5":
        conta.verificar_saldo()
    elif opcao == "6":
        novo_limite = float(input("Digite o novo limite: "))
        conta.alterar_limite(novo_limite)
    elif opcao == "0":
        print("Encerrando programa de acesso a conta bancária...")
    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")