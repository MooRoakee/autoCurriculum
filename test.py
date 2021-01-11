import pyautogui as au

x, y = au.locateCenterOnScreen('red_dot.png', confidence=0.9)
au.moveTo(x + 90, y + 80)
