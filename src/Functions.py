import random
import pyautogui as auto


def moveTo(x, y, dur):
    auto.moveTo(x, y, duration=dur)
    return


def click(dur):
    auto.click(duration=dur)


def getRandInt(num1, num2):
    return random.randint(num1, num2)


def getDuration(num1, num2):
    return round(random.uniform(num1, num2), 6)
