import sys
import multiprocessing as mp
import keyboard
import pyautogui as auto
import cv2 as cv
import numpy as np
import random
import time

from RectCoords import RectCoords
from src.Constants import *
from src.Functions import *

"""
import pyautogui as au
au.displayMousePosition()
"""

def verificarInicio():
    if auto.locateOnScreen("../imgs/duck.png", region=POS_ENTRY_PARAMS, confidence=0.7):
        moveTo(getRandInt(POS_ENTRY.getx1(), POS_ENTRY.getx2()),
               getRandInt(POS_ENTRY.gety1(), POS_ENTRY.gety2()),
               getDuration(0.1, 3))
        click(getDuration(0.1, 0.75))
        print("found duck")
        time.sleep(5)
    if auto.locateOnScreen("../imgs/Puntodeviaje.png", region=POS_PUNTOVIAJE_PARAMS, confidence=0.7):
        moveTo(getRandInt(BT_PUNTOVIAJE[0], BT_PUNTOVIAJE[2]),
               getRandInt(BT_PUNTOVIAJE[1], BT_PUNTOVIAJE[3]),
               getDuration(0.1, 2))
        click(getDuration(0.1, 0.75))
        print("found punto de viaje")
        time.sleep(5)
    return


def main():
    print("Llega al main")
    print(POS_ENTRY_PARAMS)
    while True:
        verificarInicio()
    return


if __name__ == '__main__':
    time.sleep(1)
    main()

    sys.exit(0)
