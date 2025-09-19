import os
os.system("cls")

preco_total = 0
while True:
    print("""
------------------- MENU -----------------
|  Codigo   |      Prato       |  Valor  |
|========================================|
|     1     |     Picanha      |R$ 25.00 |
|     2     |     Lasanha      |R$ 20.00 |
|     3     |    Strogonoff    |R$ 18.00 |
|     4     |  Bife acebolado  |R$ 15.00 |
|     5     |    Pão com ovo   |R$ 5.00  |
------------------------------------------
""")
    opcao = int("Digite sua escolha ")
    match opcao:
        case 1:
            codigo = "1"
            nome = "Picanha"
            valor = 25
        case 2:
            codigo = "2"
            nome = "Lasanha"
            valor = 20
        case 3:
            codigo = "3"
            nome = "Strogonoff"
            valor = 18
        case 4:
            codigo = "4"
            nome = "Bife acebolado"
            valor = 15
        case 5:
            codigo = "5"
            nome = "Pão com ovo"
            valor = 5
        case _:
            print("Opção invalida.")
            print("Tente novamente...")
            valor = 0
    preco_total += valor
