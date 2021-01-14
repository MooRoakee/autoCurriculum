import pyautogui as au
import time

SLEEP_TIME = 30
con = 'continue.png'
red_dot = 'red_dot.png'
pause = 'pause.png'


def click_continue_dialog():
    try:
        x, y = au.locateCenterOnScreen(con, confidence=0.3)
        au.click(x, y + 210)
    except TypeError:
        print("cant find continue dialog")


def click_red_dot():
    try:
        x, y = au.locateCenterOnScreen(red_dot, confidence=0.9)
        au.click(x + 90, y + 80)
    except TypeError:
        print("cant find red dot")


def down_count(x):
    print("count down: ")
    print("%d " % x, end="")
    while x:
        time.sleep(1)
        x = x - 1
        print("%d " % x, end="")
    print()


def if_finish():
    try:
        x, y = au.locateCenterOnScreen(pause, confidence=0.9)
        click_red_dot()

        time.sleep(2)
        click_tips()
    except TypeError:
        return


def click_tips():
    au.click(1230, 1162)


if __name__ == "__main__":
    while 1:
        time.sleep(2)
        if_finish()

        down_count(280)

        down_count(SLEEP_TIME)

        click_continue_dialog()
