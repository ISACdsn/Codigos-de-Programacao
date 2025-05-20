import random 

while True:

    letras = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i' ,'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'

    letra_digitada = input('Qual letra vai se digitada?')

    letra_escolhida = random.choice(letras)
    print(letra_digitada)
    print(letra_escolhida)

    if letra_digitada == letra_escolhida:
        acertou = print('EU ACERTEI A SUA LETRA!!!!  VOCÊ É AZARADO KKKKKKKK')
        break
        
    else:
        errou = print('Quase acertei sua letra')
        continue