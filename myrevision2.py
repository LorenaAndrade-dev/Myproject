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