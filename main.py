import pyautogui as p
import time as t


counter = 0
for i in range(2):
    t.sleep(1)
    print(i)


while True:
    p.hotkey('ctrl','p')
    t.sleep(1)

    p.press('tab')
    #t.sleep(0.5)
    p.press('tab')
    #t.sleep(0.5)
    p.press('tab')
    #t.sleep(0.5)
    p.press('tab')
    #t.sleep(0.5)
    p.press('tab')
    #t.sleep(0.5)
    p.press('enter')
    #t.sleep(0.5)
    p.press('down')
    #t.sleep(0.5)
    p.press('down')
    #t.sleep(0.5)
    p.press('down')
    #t.sleep(0.5)
    p.press('enter')
    t.sleep(0.5)
    p.press('1')
    t.sleep(0.5)
    p.press('enter')
    t.sleep(0.5)
    p.typewrite(str(counter))
    t.sleep(0.5)
    p.typewrite(".pdf")
    p.press("enter")
    t.sleep(0.5)
    p.press("right")
    t.sleep(0.5)
    counter = counter + 1
    if counter == 705:
        break
