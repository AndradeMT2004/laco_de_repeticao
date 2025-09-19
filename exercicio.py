import os
os.system("cls")

quantidade_notas = 0
nota_final = 0
contador = 0
while True:
    add_nota = input("Deseja adicionar mais uma nota? (s/n): " ).lower()
    if add_nota == "n":
        break
    elif add_nota == "s":
        nota = int(input("Digite a sua nota: "))
        nota_final += nota
        quantidade_notas += 1
        contador += 1

        if quantidade_notas > 0:
            media = nota_final/quantidade_notas
            print(f"Média atual: {media:.2f}")
            print(f"Iterações realizadas: {contador}")  # Exibe o contador de iterações
    else:
         print("Resposta inválida! Por favor, digite 's' para sim ou 'n' para não.")

         