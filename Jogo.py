import random

# Acerte o número aleatório

numero = random.randint(1,10)

acertou = False

while acertou == False:
    palpite = int(input("Digite um valor de 1 a 10: "))
    if (palpite == numero):
        print("Parabéns!! Você acertou")
        acertou = True
    elif (palpite < 10 and palpite != numero):
        print(f"Tente novamente(O valor era {numero})")
        numero = random.randint(1,10)
    else: 
        print("Digite um valor de 1 a 10")
        numero = random.randint(1,10)
print("Fim do jogo!")