#  Funcao calculaDistancia
# criaria 2 lista 
# funcao verifica numeros
# variavel posicao 
# resultado #/


# x =  list [1, 2, 3, 4, 5 ]
# y = list [ 6, 7, 8, 9, 10,]
# z = list

# Resultado = z
# if x >= y:
    # print("Resultado")


import sys

def menor_distancia(array1, array2):
    menor = sys.maxsize  # Inicializa a menor distância com um valor grande

    for num1 in array1:
        for num2 in array2:
            # Calcula a distância absoluta entre os números
            distancia = abs(num1 - num2)

            # Atualiza a menor distância se a distância calculada for menor
            if distancia < menor:
                menor = distancia

    return menor

# Exemplo de uso
array1 = [100, 200, 23, 12, 90, 25, 37, 35, 551, 45]
array2 = [260, 6, 10, 15, 18, 28, 32, 38, 42, 50]

resultado = menor_distancia(array1, array2)
print(f"A menor distância é: {resultado}")
