def filtro(numeros,condicion):
    resultado= []
    for numero in numeros:
        if condicion(numero):
            resultado.append(numero)
    return resultado

def es_par(numero):
    return numero % 2 == 0

def es_positivo(numero):
    return numero > 0

numeros = [1, 2, 3, 4, 5, 6]

print(filtro(numeros, es_par))

print(filtro(numeros, es_positivo))

def suma(*args):
    print(type(args))
    return sum(args)

print(suma(1,2))
print(suma(1,2,3))
print(suma(1,2,1,2,-1,-7))