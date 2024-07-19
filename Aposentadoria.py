#Para saber se já se aposentou:

sexo = (input("Digite seu sexo( Digite Feminino ou Masculino): "))
idade = int(input("Digite sua idade: "))
tempo = int(input("Digite o tempo de contribuição: "))

if sexo =="Feminino" and idade >= 62 or tempo >= 32:
    print(" Já pode ser aposentar.")
elif sexo == "Masculino" and idade >= 65 or tempo >= 35:
    print(" Já pode se aposentar.")
else:
    print("Ainda faltam requisitos")





