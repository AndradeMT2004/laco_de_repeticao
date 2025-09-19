import os
os.system("cls")

soma = 0
quantidade_notas = 0
while True:
    nota = float(input("Digite uma nota: "))
    if nota < 0:
        break
    quantidade_notas += 1
    soma += nota
    media = soma/quantidade_notas  

  
    
print(f"\nMedia aritmética = {media}")