numero=0
operador=""
acumulador=0
while operador != "fin":
    numero=int(input("escribir numeros"))
    if numero > acumulador:
        acumulador = numero
    operador=input("desea seguir o fin")
print(acumulador)
