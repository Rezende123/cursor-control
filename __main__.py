from pynput import keyboard
from services.control import controlMouseWithKeys
from services.image_detector import detect_face

def on_press_key(tecla):
    try:
        # print("Tecla pressionada: {0}".format(tecla))
        controlMouseWithKeys(tecla)
    except AttributeError:
        print("Tecla especial pressionada: {0}".format(tecla))

def main():
    print("Para controlar o mouse use as teclas W(cima) A(esquerda) S(direita) D(baixo)\n")
    
    with keyboard.Listener(on_press=on_press_key) as listener:
        listener.join()

# main()
detect_face()

