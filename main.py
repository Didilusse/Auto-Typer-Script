import pyautogui as pg
import time

time.sleep(5)

a = "Get On Skyblock"

t_end = time.time() + 10
while time.time() < t_end:
    pg.write(a)
    time.sleep(0.1)
    pg.press('Enter')
    print('sent')
