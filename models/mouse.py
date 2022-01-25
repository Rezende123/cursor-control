import pyautogui

class Mouse:
    def __init__(self):
        screenWidth, screenHeight = pyautogui.size()
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

    def move(self, x, y):
        pyautogui.move(x, y)

    def moveTo(self, x, y):
        pyautogui.moveTo(x, y)

    def moveRel(self, x, y):
        pyautogui.moveRel(x, y)

    def click(self, x, y):
        pyautogui.click(x, y)

    def dragTo(self, x, y):
        pyautogui.dragTo(x, y)

    def dragRef(self, x, y):
        pyautogui.dragRel(x, y)

    def position(self, ):
        return pyautogui.position()

