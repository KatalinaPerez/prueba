'''Ingresar por teclado 5 números enteros, luego debe indicar:
• Cuántos números son mayores a cero
• Cuántos números son menores a cero
• Cuántos números son iguales a cero'''
contpositivo=0
contnegativo=0
contcero=0
for i in range(1,6):
    print (f"Ingrese un N° {i}")
    num=int(input())
    if num==0:
        contpositivo+=1
    elif num<0:
        contnegativo+=1
    else:
        contcero+=1
print (f"Hay {contpositivo} numeros positivos")
print (f"Hay {contnegativo} numeros negativo")
print (f"Hay {contcero} numeros iguales a cero")