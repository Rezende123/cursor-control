from pynput import keyboard
from models.mouse import Mouse


def controlMouseWithKeys(tecla):
    defTargetMove = 10
    mouse = Mouse()
    
    if tecla == keyboard.KeyCode.from_char('w'):
        mouse.move(0, -defTargetMove)
    elif tecla == keyboard.KeyCode.from_char('a'):
        mouse.move(-defTargetMove, 0)
    elif tecla == keyboard.KeyCode.from_char('d'):
        mouse.move(defTargetMove, 0)
    elif tecla == keyboard.KeyCode.from_char('s'):
        mouse.move(0, defTargetMove)
