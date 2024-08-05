#Demonstração do uso de estrutura repetitiva...
contador = 0; senha = ""
while senha != "S3nh4":
    print("Digite sua senha:")
    senha = input()

    if senha == "S3nh4":
        print("Senha correta!")
        break
    else:
        print("Senha incorreta")

    contador = contador + 1
    if contador == 3:
        print(" Tentativas excedidas!")
        break
