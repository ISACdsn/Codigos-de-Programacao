num1 = int(input("Primeiro valor:"))
num2 = int(input("Segundo valor:"))

opção = 0

while opção !=5:
    print("""O que você quer fazer com seus numeros?
          [1] Somar
          [2] Multiplicar
          [3] Maior
          [4] Trocar de numero
          [5] Encerrar o prgrama""")
    
    opção = int(input("Qual opção você quer?"))

    if opção == 1:
        soma = num1+num2
        print(f"A soma de {num1} + {num2} é {soma}")

    elif opção == 2:
        produto = num1*num2
        print(f"{num1} X {num2} é {produto}")

    elif opção == 3:
        maior = max(num1,num2)
        print(f"Entre {num1} e {num2} maior é {maior}")

    elif opção == 4:
        print("Tente novamente")
        num1 = int(input("Primeiro valor:"))
        num2 = int(input("Segundo valor:"))

print("Programa encerrado")