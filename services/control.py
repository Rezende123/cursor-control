from pynput import keyboard
from models.mouse import Mouse

def rangeConversion(old_value, olx_max, old_min, new_max, new_min):
    return (((old_value - old_min) * (new_max - new_min)) / (olx_max - old_min)) + new_min

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

def controlMouseWithFacePosition(face):
    x_position, y_position = face[0]
    X_MAX = 50
    Y_MAX = 50
    mouse = Mouse()

    x_range_position = rangeConversion(x_position, 120, 480, X_MAX, -Y_MAX)
    y_range_position = rangeConversion(y_position, 480, 120, X_MAX, -Y_MAX)

    print(x_range_position, y_range_position)
    mouse.move(x_range_position, y_range_position)