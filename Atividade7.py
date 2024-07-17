# 1. Duas notas, se média <4 "reprovado", > 6 "aprovado direto", <4>6 "recuperação". Caso recuperação 
# solicitar nota de recuperação, caso <5 " reprovado na recuperação", caso não "aprovado recuperação"

#2 algoritmo para time e sua poição na tabela de classificação, exibir campeão para 1º lugar, libertadores ( entre 1 e 6)
#Sul america (entre 7 e 12) e rebaixado os demais

#digitar 3 numeros distintos,sendo armazenados nas variavei x y z, informar se estão em ordem crescente ou decrescente, 
# se não exibir  numeros misturados


# 1 .
nota1 = float(input("Digite sua nota 1 aqui:"))
nota2 = float(input("Digite sua nota 2 aqui:"))
media = nota1 + nota2 /2
print(f"Sua média é de:{media}")


if media < 4:
    print( "Reprovado")
elif media > 6:
    print( "Aprovado direto")
else:
    print( "Recuperação")
    



