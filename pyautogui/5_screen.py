import pyautogui

img = pyautogui.screenshot()
img.save("screenshot.png")

pixel = pyautogui.pixel(28, 18)
print(pixel)

print(pyautogui.pixelMatchesColor(28, 18, pixel))
