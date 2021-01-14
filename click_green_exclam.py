import time
import pyautogui as au

from autoPartyClass import down_count

con = 'continue.png'


def click_green_exc():
    try:
        x, y = au.locateCenterOnScreen(con, confidence=0.8)
        au.click(x, y + 210)
    except TypeError:
        print("cant find continue dialog")


if __name__ == '__main__':
    while 1:
        down_count(10)
        click_green_exc()
