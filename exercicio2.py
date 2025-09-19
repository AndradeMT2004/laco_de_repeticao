import os
os.system("cls")

soma = 0
quantidade_notas = 0

while True:
    nota = float(input("Digite a sua nota: "))   
    quantidade_notas += 1
    soma += nota
    resposta = input("Deseja inserir mais uma nota? \nuse S ou N: ").lower()
    if resposta == "n":
        break
media = soma/quantidade_notas

print(f"\nmedia = {media}")
         