num1 = int(input("Primeiro valor:"))
num2 = int(input("Segundo valor:"))
opcao = 0
while opcao !=5:
    print("O que você quer fazer com esses números? [1] Somar  [2] Multiplicar  [3]Maior  [4]Trocar de número   [5] Encerrar o programa")
    opcao = int(input("Qual opcao você quer?"))
    if opcao == 1:
        soma = num1+num2
        print(f"A soma de {num1} + {num2} é {soma}")

    elif opcao == 2:
        produto = num1*num2
        print(f"{num1} X {num2} é {produto}")

    elif opcao == 3:
        maior = max(num1,num2)
        print(f"Entre {num1} e {num2} maior é {maior}")

    elif opcao == 4:
        print("Tente novamente")
        num1 = int(input("Primeiro valor:"))
        num2 = int(input("Segundo valor:"))
    
print("Programa encerrado.")