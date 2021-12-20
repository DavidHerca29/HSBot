import random


def getRandInt(num1, num2):
    return random.randint(num1, num2)

def getDuration(num1, num2):
    return round(random.uniform(num1, num2), 6)