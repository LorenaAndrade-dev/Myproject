#Sistema de avaliação de serviços

servico = (input("O serviço foi prestado?")):

if  servico == "não":
    print(input(" Digite aqui a sua reclamação:"))
elif servico == "sim":
    nota = (input(" Digite a sua nota de 1 à 5:")):
    if nota == 1:
        print(" Péssimo atendimento")
    elif nota == 2:
        print("Ruim")
    elif nota == 3:
        print("Razoável")
    elif nota == 4:
        print(" Bom")
    elif nota == 5:
        print ("Ótimo")



print( "Obrigado por escolher nossos serviços!")