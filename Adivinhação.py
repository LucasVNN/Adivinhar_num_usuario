from random import randint
from time import sleep

def tempo(a, temp):
    from time import sleep
    if temp == 'max':
        print('.', end='')
        sleep(1.5)
        print('.', end='')
        sleep(1.5)
        print('.')
        sleep(1.5)
    else:
        print('.', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.')
        sleep(0.5)


userpot = pcpont = cont = 0
print(f"\033[47m{'ADIVINHAÇÃO': ^50}")
print('\033[m')
while True:
    numero_user = int(input("Escolha um número: "))
    for c in range(1, 3):
        numero_pc = randint(1, 10)
        if numero_pc == numero_user:
            pcpont +=1
            tempo(True, 'min')
            print(f"Você escolheu {numero_user} e a máquina também escolheu {numero_pc}")
            print("A máquina acertou!!")
            break
        else:
            userpot+=1
            if cont == 0:
                tempo(True, 'min')
                cont+=1
            print(f"Você escolheu {numero_user} e a máquina escolheu {numero_pc}")
            print("\033[34mA máquina errou!!\033[m")
            if c == 2:
                break
            sleep(0.5)
            print("\033[4mEspere! A máquina está fazendo outra jogada\033[m", end='')
            tempo(True, 'max')
    if pcpont > 0:
        print("\033[41;1mVOCÊ PERDEU!!\033[m")
    else:
        print("\033[44;1mVOCÊ GANHOU!!\033[m")
    resp = str(input("Você quer continuar? [S/N]")).upper()[0]
    pcpont = 0
    if resp == 'N':
        break
