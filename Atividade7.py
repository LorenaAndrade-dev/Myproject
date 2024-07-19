# 1. Duas notas, se média <4 "reprovado", > 6 "aprovado direto", <4>6 "recuperação". Caso recuperação 
# solicitar nota de recuperação, caso <5 " reprovado na recuperação", caso não "aprovado recuperação"

#2 algoritmo para time e sua posição na tabela de classificação, exibir campeão para 1º lugar, libertadores ( entre 1 e 6)
#Sul america (entre 7 e 12) e rebaixado os demais

#digitar 3 numeros distintos,sendo armazenados nas variavei x y z, informar se estão em ordem crescente ou decrescente, 
# se não exibir  numeros misturados


# 1 .
nota1 = float(input("Digite sua nota 1 aqui:"))
nota2 = float(input("Digite sua nota 2 aqui:"))
media = nota1 + nota2 /2
print(f"Sua média é de:{media}")

if media < 4:
    print("Reprovado")
elif media >= 4 and media < 6:
    print( "Recuperação")
    recuperacao = float(input("Digite a nota da recuperação:"))
    if recuperacao < 5:
        print ("Reprovado na recuperação")
    else:
        print(" Aprovado na recuperação")
else:
    print("Aprovado")

    
#2.
time = input(" Digite seu time:")
posicao = int(input(" Digite a posição do seu time:"))

if posicao == 1:
    print (" Campeão")
elif posicao >=2 and posicao <=6:
    print("Libertadores")
elif posicao >= 7 and posicao ==12:
    print(" Sul - Americana")
else:
    print("Rebaixado")










# 3.
x = int(input(" Digite o primeiro número:"))
y = int(input("Digite o segundo número:"))
z = int(input("Digite o terceito número:"))

if x > y and y > z:
    print(" Números em ordem decrescente")
elif x < y and y < z :
    print(" Números em ondem cescente")
else:
    print ("Números misturados")


