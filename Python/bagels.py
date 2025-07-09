import random
print("""Bagels, um jogo de dedução lógica.\nEstou pensando em um número de 3 dígitos. Tente adivinhá-lo. Algumas pistas:
Quando eu disser:\tSignifica:\n\tPico\t\tUm dígito está correto mas na posição errada.
\tFermi\t\tUm dígito está correto e na posição certa.
\tBagels\t\tNenhum dígito está correto.\nPensei um número.\nVocê tem 10 palpites para adivinhá-lo.""")

def gerar_numero():
    numero1 = random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    numero2 = random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    numero3 = random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    numero = numero1 + numero2 + numero3
    return numero

contador = 1
palpite = ""
numero_aleatorio = gerar_numero()

while contador < 11:
    palpite = input(f"Palpite {contador}\n")
    contador += 1
    if palpite == numero_aleatorio:
        print("Parabéns, você acertou!")
        continuar =input("Deseja jogar novamente? (S/N) ")
        if continuar.lower() == "s":
            contador = 1
            numero_aleatorio = gerar_numero()
            continue
        else:
            print("Obrigado por jogar!!")
            break
    elif palpite[0] == numero_aleatorio[0] or palpite[1] == numero_aleatorio[1] or palpite[2] == numero_aleatorio[2]:
        print("Fermi")
    elif palpite[0] in numero_aleatorio or palpite[1] in numero_aleatorio or palpite[2] in numero_aleatorio:
        print("Pico")
    else:
        print("Bagels")
#print(f"O número era {numero_aleatorio}!")
    
