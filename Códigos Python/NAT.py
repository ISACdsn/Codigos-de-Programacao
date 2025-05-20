import random 

while True:

    numeros = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'

    numero_digitado = input('Entre 0 ao 9, Qual o numero vai ser digitado?')
    
    numero_escolhido = random.choice(numeros)
    print(numero_digitado)
    print(numero_escolhido)

    if numero_digitado == numero_escolhido:
        print('EU ACERTEI SEU NUMEROKKKKKKKK')
        break

    else:
        print('Eu quase acertei sua numero')
        continue