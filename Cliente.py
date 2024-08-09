#Criar programa para cadastro de clientes, com nome, idade, id ou cpf,valor de abertura de conta.

nome = input("Digite seu nome completo:")
idade = int(input("Digite a sua idade:"))
id = int(input("Digite o número da identidade ou cpf, sem os pontos:"))
valorinicial = float(input("Digite o valor para abertura de conta:"))

if idade <18:
    print("Voce é menor de idade, não pode abrir conta no seu nome.")
elif idade >= 18 and idade < 65:
    print("Você pode abrir uma conta conosco!")
elif idade >= 65:
    print("Você já está se preparando para aposentar!")
else:
    print(" Opção inválida.")


print(f"Olá {nome}! Seja bem vindo(a)! Sua idade é de {idade}, sua identidade ou cpf é {id}. O valor inicial da abertura é de {valorinicial}.")
