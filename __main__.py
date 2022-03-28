from pynput import keyboard
from services.control import controlMouseWithKeys
from services.control import controlMouseWithFacePosition
from services.image_detector import detect_face

def on_press_key(tecla):
    try:
        # print("Tecla pressionada: {0}".format(tecla))
        controlMouseWithKeys(tecla)
    except AttributeError:
        print("Tecla especial pressionada: {0}".format(tecla))

def keyboard_control():
    print("Para controlar o mouse use as teclas W(cima) A(esquerda) S(direita) D(baixo)\n")
    
    with keyboard.Listener(on_press=on_press_key) as listener:
        listener.join()

# keyboard_control()

def main():
    while True:
        face = detect_face()

        if face.any():
            print(f"FACE DETECTADA")
            controlMouseWithFacePosition(face)
main()
