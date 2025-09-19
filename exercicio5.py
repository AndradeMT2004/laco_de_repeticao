import os

quantidade_num = 0
soma = 0
impar = 0
par = 0
resultado_par = 0
resultado_impar = 0
while True:
    num = int(input("Digite um numero: "))
    quantidade_num +=1
    if num % 2 == 0:
        resultado_par += par
        par += 1
    else:
        resultado_impar =+ impar
        impar += 1
    soma =+ num
    media = par + impar
    mediapar = quantidade_num - impar
    if num == 0:
        break
print(f"A quantidade geral de numeros é {quantidade_num}")
print(f"A media de valores pares é {mediapar}")
print(f"A media geral dos numeros lidos é {media}")
print(par)
print(impar)


