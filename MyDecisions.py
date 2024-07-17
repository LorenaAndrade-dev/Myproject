# Demostração de operadores lógicos em condicionais..

print("O que você vai fazer amanhã de manhã?")
print(" Dormir/ estudar / planejar")
manha = input()
print(" O que você vai fazer amanhã de tarde?")
print(" jogar / treinar / trabalhar")
tarde = input()

if not manha or not tarde:
    print(" Você precisa dizer o que vai fazer")
else:
    if manha == "dormir" or tarde == "jogar":
        print(" Você está descansando né?")
    elif manha == "estudar" or tarde ==" treinar":
        print("Que bom! Você está se aperfeiçoando.")
    elif manha == "planejar" and tarde == "trabalhar":
        print("Para trabalhar melhor, devo planejar")
    else:
        print("Não combinamos essas ações..")

print(" Tenha um bom dia!")