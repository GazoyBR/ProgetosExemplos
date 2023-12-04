def eh_palindromo(palavra):
    palavra = palavra.lower()  # Converte a palavra para minúsculas
    palavra = palavra.replace(" ", "")  # Remove espaços em branco
    return palavra == palavra[::-1]

# Exemplo de uso
palavra_digitada = input("Digite uma palavra: ")
if eh_palindromo(palavra_digitada):
    print(f"{palavra_digitada} é um palíndromo!")
else:
    print(f"{palavra_digitada} não é um palíndromo.")

