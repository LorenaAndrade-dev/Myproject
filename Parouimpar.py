#Criar par ou impar,usar função para resolver o jogo. se der par, usuario 1 vence, se der impar computador vence.

def parouimpar():
    n1 = int(input(" Jogador, escolha seu número:"))
    n2 = int(input("Computador, escolha seu número:"))
soma = n1 +n2
vencedor = " Computador" if soma% 2 == 0 else "Jogador"
