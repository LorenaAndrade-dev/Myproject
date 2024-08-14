#Demonstração de métodos em listas
inss = ["Maria", " Manoel", "José", "Isabella"]
print("Eis a fila do Inss:", inss)

novo = input("Insira mais uma pessoa:")
inss.append(novo)
print("conferindo a nova lista: ", inss)

print("Vou tirar a ultima pessoa")
especial = inss.pop()

print("Agora vou colocá-la na frente de todos")
inss.inset(0, especial)
print("Conferindo a lista: ", inss)

print("Maria não gostou e reclamou")
inss.renove("Maria")
print("E agora ela esta fula da vida", inss)

print("Para não ter mais reclamação, vamos atender")
inss.sort()
print("... em ordem alfabética:", inss)

print("Onde está a nova pessoa chamda", especial,"?")
print("Ela ficou na posição", inss.index(especial)+1, "!")