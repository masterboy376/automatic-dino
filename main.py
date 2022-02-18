import pyautogui
from PIL import Image, ImageGrab
import time

def pressKey(key):
    pyautogui.keyDown(key)

def isCollide(data):
    # for i in range(470, 475):
    #     for j in range(210,233):
    #         if data[i,j]>100:
    #             pressKey("down")
    #             return

    for i in range(530,535):
        for j in range(233,270):
            if data[i,j]>100:
                pressKey("up")
                return
    for i in range(455,460):
        for j in range(233,270):
            if data[i,j]>100:
                pressKey("up")
                return
    return

if __name__ == '__main__':
    time.sleep(2)
    pressKey("space")
    while True: 
        image = image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

    # image = image = ImageGrab.grab().convert('L')
    # data = image.load()
    # for i in range(455, 460):
    #     for j in range(233,270):
    #         data[i,j]=0
    # for i in range(530, 535):
    #     for j in range(210,233):
    #         data[i,j]=100
    # image.show()


