from models.mouse import Mouse

defTargetMove = 10

def controlMouse(tecla):
    mouse = Mouse()
    
    if tecla == "W":
        mouse.move(0, -defTargetMove)
    elif tecla == "A":
        mouse.move(-defTargetMove, 0)
    elif tecla == "D":
        mouse.move(defTargetMove, 0)
    elif tecla == "S":
        mouse.move(0, defTargetMove)
