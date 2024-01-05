print("Programa de Cálculo de Ganhos mensais")

fixo = float(input("Qual valor base do seu salário: "))
vendas = float(input("Digite o valor total de suas vendas: "))
comicao = float(input(f"Digite sua comissão: ")) / 100.0
Ganhos = fixo + vendas * comicao

print(f"Seu lucro é de {Ganhos}")