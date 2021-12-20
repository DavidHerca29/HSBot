import sys
import multiprocessing as mp
import keyboard
import pyautogui as auto
import cv2 as cv
import numpy as np
import random
import time
from RectCoords import RectCoords
from src.Functions import *

POS_ENTRY_PARAMS = (730, 189, 1002, 337)
POS_ENTRY = RectCoords()
POS_ENTRY.setRect(730, 189, 1002, 337)

def test():
    return


def verificarInicio():
    if auto.locateOnScreen("../imgs/duck.png", region=POS_ENTRY_PARAMS, confidence=0.6):
        auto.moveTo(getRandInt(POS_ENTRY.getx1(), POS_ENTRY.getx2()),
                    getRandInt(POS_ENTRY.gety1(), POS_ENTRY.gety2()),
                    duration=getDuration(0.1, 4))
        auto.click(duration=getDuration(0.1, 0.8))
    return


def main():
    print("Llega al main")
    print(POS_ENTRY_PARAMS)
    while True:
        verificarInicio()
    test()
    return


if __name__ == '__main__':
    time.sleep(1)
    main()

    sys.exit(0)
