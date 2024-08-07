#Demonstração do uso de funções

def apresentar():
    print("Meu nome é", nome, ".")
    print("Minha altura é de", altura,"metros.")
    print("Minha idade é", idade, "anos.")
    return
def conferir(x):
    if x >= 18:
        print("Você é maior de idade!")
    else:
        print("Ops, menor de idade não pode!")
        return
    
nome = str(input("Digite seu nome: "))
altura = float(input("Digite sua altura: "))
idade = int(input("Digite sua idade: "))

apresentar()
conferir(idade)