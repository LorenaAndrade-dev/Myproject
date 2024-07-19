#informar função no campo


funcao = (input("Digite aqui a sua função dentro de campo:"))
if funcao == "Goleiro" or funcao =="Zagueiro" or  funcao ==" Lateral":
    print("Defesa")
elif funcao == "Volante" or  funcao =="Meia":
    print("Meio - Campo")
elif funcao == "Ponta" or funcao =="Atacante" or funcao == " Centoavante":
    print("Ataque")
else:
    print("Teimoso")