#Demosntração do uso da condicional match/case
print("Digite o número referente ao estado da moeda:")
print("1. Flor de cunho")
print("2. Soberba")
print("3. Muito bema conservada")
print("4. Bem conservada")
print("5. Outros estados")
estado = int(input())

match estado:
    case 1:
        print(" Perfeito! Vou pagar R$ 1.000.00,00!")
    case 2:
        print("Quase perfeita! Ofereço R$ 250.000,00!")
    case 3:
        print("Que ótimo! Posso te oferecer R$ 100.000,00")
    case 4:
        print("Que bom, aceitaria R$ 300.00,00?")
    case 5:
        print("Desculpe, não posso aceitar nesse estado.")
    case _:
        print("Opção não reconhecida")


