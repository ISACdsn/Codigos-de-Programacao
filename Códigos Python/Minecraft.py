import time
acertou = 0
errou = 0

per = input("Qual mob que consegue subir paredes?")
if per == "Aranha" or per == "aranha":
    print("Oloko, acertou")
    acertou += 1
else:
    print("que pena, você errou")
    errou += 1

per1 = input("Qual mob no Minecraft atira flecha?")
if per1 == "Esqueleto" or per1 == "esqueleto":
    print("Oloko, acertou")
    acertou += 1
else:
    print("que pena, você errou")
    errou += 1

per2 = input("Qual mob que explode perto do player?")
if per2 == "Creeper" or per2 == "creeper":
    print("Oloko, acertou")
    acertou += 1
else:
    print("que pena, você errou")
    errou += 1

per3 = input("Qual mob que defende os Villages?")
if per3 == "Iron golem" or per3 == "iron golem":
    print("Oloko, acertou")
    acertou += 1
else:
    print("que pena, você errou")
    errou += 1

per4 = input("Qual item nós fazemos trocas com os Villages?")
if per4 == "Esmeralda" or per4 == "esmeralda":
    print("Oloko, acertou")
    acertou += 1
else:
    print("que pena, você errou")
    errou += 1

per5 = input("Qual é a picareta que quebra muito rápida do que as outras?")
if per5 == "Picareta de ouro" or per5 == "picareta de ouro":
    print("Oloko, acertou")
    acertou += 1
else:
    print("que pena, você errou")
    errou += 1

per6 = input("Qual mob que bota ovo?")
if per6 == "Galinha" or per6 == "galinha":
    print("Oloko, acertou")
    acertou += 1
else:
    print("que pena, você errou")
    errou += 1

per7 = input("Qual é o nome da amiga do Steve?")
if per7 == "Alex" or per7 == "alex":
    print("Oloko, acertou")
    acertou += 1
else:
    print("que pena, você errou")
    errou += 1

per8 = input("Qual mob que expanda os Creepers?")
if per8 == "Gato" or per8 == "gato":
    print("Oloko, acertou")
    acertou += 1
else:
    print("que pena, você errou")
    errou += 1

per9 = input("Qual mob que dá lã?")
if per9 == "Ovelhas" or per9 == "ovelhas":
    print("Oloko, acertou")
    acertou += 1
else:
    print("que pena, você errou")
    errou += 1

per10 = input("Qual mob que pega e dá mel?")
if per10 == "Abelha" or per10 == "abelha":
    print("Oloko, acertou")
    acertou += 1
else:
    print("que pena, você errou")
    errou += 1

print("Parabéns você terminou as Perguntas de Minecraft")
maior = max(acertou,errou)
if acertou >= errou:
 print(f"Entre acertou:{acertou} e errou:{errou}, Você acertou mais do que errou")

if errou >= acertou:
 print(f"Entre acertou:{acertou} e errou:{errou}, Você errou do que acertou")

p = input("Gostou das perguntas")
if p == "Sim" or p == "sim":
    print("Estou feliz com essa resposta")
    time.sleep(3)
else:
    print("Caguei com sua resposta")
    time.sleep(5)

print("ACABOU")
time.sleep(3)