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
print("Digite as notas aqui:")
nota1 = int(input())
nota2 = int(input())
nota3 = int(input())
media = nota1 + nota2 + nota3 / 3

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")


#3.
print("Digite seu peso:")
peso = int(input())
print("Digite sua altura:")
altura = int(input())
icm = peso / altura

if icm > 25:
    print("Acima do peso ideal")
elif icm < 18:
    print("Abaixo do peso ideal")
else:
    print("Seu peso está ok.")

