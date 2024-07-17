# 1. dia da semana
# 2. notas trimestrais, média, aprovado ou reprovado
# 3. peso e altura, icm acima ou não

# 1. 
print("Digite o dia da semana:")
print("Segunda")
print("Terça")
print("Quarta")
print("Quinta")
print("Sexta")
dia = input()

match dia:
    case "Segunda":
        print("Dia de lavar roupa")
    case "Terça":
        print("Dia de Lavar a cozinha") 
    case "Quarta":
        print("Dia de varrer a casa")
    case "Quinta":
        print("Dia de lavar banheiro") 
    case "Sexta":
        print("Sextou!") 
    case _:
        print("É final de semana, vai descansar!") 


#2.
nota1 = float(input("Digite a nota 1 aqui: "))
nota2 = float(input("Digite a nota 2 aqui: "))
nota3 = float(input("Digite a nota 3 aqui: "))
nota4 = float(input("Digite a nota 4 aqui: "))
media = nota1 + nota2 + nota3 + nota4 / 4

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")

print(f"Sua média é {media}")
print(type(media))

#3.
print("Digite seu peso:")
peso = int(input())
print("Digite sua altura:")
altura = float(input())
icm = peso / altura ** 2 

if icm > 25:
    print("Acima do peso ideal")
elif icm < 18:
    print("Abaixo do peso ideal")
else:
    print("Seu peso está ok.")