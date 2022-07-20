import pyautogui
# pyautogui.FAILSAFE=False #강제종료 방지
pyautogui.PAUSE = 1  # 모든 동작에 1초씩 sleep
# pyautogui.mouseInfo()

for i in range(10):
    pyautogui.move(100, 100)
# 커서를 양쪽 코너에 놔두면 프로그램 강제종료
