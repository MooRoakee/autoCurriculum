import pyautogui as au
import time

SLEEP_TIME = 60
con = 'continue.png'
red_dot = 'red_dot.png'
pause = 'pause.png'


def click_continue_dialog():
    try:
        x, y = au.locateCenterOnScreen(con, confidence=0.3)
        au.click(x, y + 55)
    except TypeError:
        print("cant find continue dialog")


def click_red_dot():
    try:
        x, y = au.locateCenterOnScreen(red_dot, confidence=0.9)
        au.click(x + 100, y + 40)
    except TypeError:
        print("cant find red dot")


def down_count(x):
    print("count down: ")
    print("%d " % x)
    while x:
        time.sleep(1)
        x = x - 1
        print("%d " % x, end="")
    print()


def if_finish():
    try:
        x, y = au.locateCenterOnScreen(pause, confidence=0.9)
        au.click(769, 653)
        click_red_dot()


        time.sleep(2)
        click_begin()
    except TypeError:
        return


def click_begin():
    try:
        x, y = au.locateCenterOnScreen(con, confidence=0.3)

        au.click(995, 669)
    except TypeError:
        exit()


if __name__ == "__main__":
    while 1:
        if_finish()

        down_count(SLEEP_TIME)

        click_continue_dialog()
