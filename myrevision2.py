# Revisão geral

print("Digite o seu nome:")
nome = input()
idade = input("Digite a idade:")
altura = input("Digite a altura:")

print(f"Meu nome é {nome},")
print(f"Minha idade é {idade},")
print(f"e a minha altura é {altura}.")

print("Qual será a minha idade em 2036?")
tempo = 2036 - 2024
idade = idade + tempo
altura = altura /2
print(" A minha idade em 2036 será:", idade)
print(" A metade da minha altura é:", altura)

print("Qual operação você deseja realizar?")
print("1. saldo, 2. Depósito, 3. Saque")
operacao = int(input("Digite uma opção:"))
saldo= 0

match operacao:
    case 1:
        print(f" O saldo total é {saldo}")
    case 2:
        deposito = float(input("Digite o valor do depósito:"))
        saldo = saldo + deposito
    case 3:
        saque = int(input("Digite o valor a ser sacado:"))
        if saque > saldo:
            print("Não poderá fazer saque maior que o saldo!")
        else:
            saldo = saldo - saque
    case _: 
        print(" Operação inexistente")
        
