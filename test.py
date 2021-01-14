import pyautogui as au

x, y = au.locateCenterOnScreen('continue.png', confidence=0.8)
au.moveTo(x, y + 210)
