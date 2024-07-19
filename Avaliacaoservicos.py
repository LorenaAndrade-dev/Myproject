#Sistema de avaliação de serviços


servico = input("O serviço foi feito? ( sim/ não):")
nota = int(input(" Digite a nota da avaliação (1/5):"))

if servico == "Sim" and nota == 1:
    print("O serviço foi péssimo.")
elif servico == "sim" and nota == 2:
    print("O serviço foi ruim.")
elif servico == "sim" and nota == 3:
    print("O serviço foi razoável.")
elif servico == "sim" and nota == 4:
    print("O serviço foi bom.")
elif servico == "sim" and nota == 5:
    print("O serviço foi exelente.")
else:
    if servico == "Não" and nota == 0 :
        print (input(" Digite a sua reclamação:"))
    else:
        print("As suas avaliações não fazem sentido")
print( "Obrigado por escolher nossos serviços!")