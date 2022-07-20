import pyautogui
'''
file_menu = pyautogui.locateOnScreen("file_menu.png")
print(file_menu)
pyautogui.click(file_menu)


trash_icon=pyautogui.locateOnScreen("trash_icon.png")
pyautogui.moveTo(trash_icon)

screen=pyautogui.locateOnScreen("screenshot.png")
print(screen)


# w3schools.com HTML자료 있는 곳
for i in pyautogui.locateAllOnScreen("checkbox.png"):
    print(i)
    pyautogui.click(i)

# 속도개선

# 1. GrayScale 30%개선, 정확도 하락
#file_menu = pyautogui.locateOnScreen("file_menu.png", grayscale=True)

# 2. 범위 지정
#file_menu = pyautogui.locateOnScreen("file_menu.png", region=(0, 0, 169, 86))
# pyautogui.moveTo(file_menu)
# pyautogui.mouseInfo()
# 0,0 169,86

# 3. 정확도 조정
#file_menu = pyautogui.locateOnScreen("file_menu.png", confidence=0.9)  # 90%의 정확도
#pyautogui.moveTo(file_menu)

# 자동화 대상이 바로 보여지지 않는 경우
file_menu = pyautogui.locateOnScreen("file_menu.png")
if file_menu:
    pyautogui.click(file_menu)
else:
    print("발견실패")
'''

import time
import sys

timeout = 10
start = time.time()
file_menu = None
while file_menu is None:
    file_menu = pyautogui.locateOnScreen("file_menu.png")
    end = time.time()
    if end - start > timeout:
        print("시간종료")
        sys.exit()

pyautogui.click(file_menu)
