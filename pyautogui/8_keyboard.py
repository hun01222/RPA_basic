import pyperclip
import pyautogui

pyautogui.write("12345")  # 영문, 숫자만 됨
pyautogui.write("Hello", interval=1)  # 1초마다 입력

pyautogui.write(["t", "e", "s", "t", "left", "left", "right",
                "l", "a", "enter"], interval=0.25)  # 키보드 방향키, 엔터

# automate the boring stff with python 에 있음. keyboard attribute

# 특수문자
pyautogui.keyDown("Shift")
pyautogui.press("4")
pyautogui.keyUp("shift")

# 조합키 (Hot key)
pyautogui.hotkey("ctrl", "alt", "shift", "a")

# 한글 입력
pyperclip.copy("안녕")

# mac: cmd+shift+option+q ~ 자동화 프로그램 종료
