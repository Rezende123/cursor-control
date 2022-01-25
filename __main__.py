from services.control import controlMouse

def main():
    print("Para controlar o mouse use as teclas W(cima) A(esquerda) S(direita) D(baixo)\n")

    tecla = input().upper()
    
    while tecla == "W" or tecla == "A" or tecla == "S" or tecla == "D" :
        controlMouse(tecla)
        tecla = input().upper()

    print("FIM!!")

main()

