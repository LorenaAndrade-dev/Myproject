#exibir fibonacci de 0 a 2mil

x = 0
y = 1
resultado = 0

while resultado < 2000:
    resultado = x + y
    x = y
    y = resultado
    if resultado > 2000:
        break
    print(resultado)