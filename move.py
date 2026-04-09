import pyautogui
import time
import random
from datetime import datetime, time as dt_time
from zoneinfo import ZoneInfo  # tylko w Pythonie 3.9+

pyautogui.FAILSAFE = False

print("Loop started at {}".format(datetime.now().time()))

warsaw_tz = ZoneInfo("Europe/Warsaw")

last_mouse_pos = pyautogui.position()
last_movement_time = time.time()

def move_mouse_randomly():
    dx = random.randint(-50, 50)
    dy = random.randint(-50, 50)
    current_x, current_y = pyautogui.position()
    screen_w, screen_h = pyautogui.size()
    new_x = max(0, min(screen_w - 1, current_x + dx))
    new_y = max(0, min(screen_h - 1, current_y + dy))
    pyautogui.moveTo(new_x, new_y, duration=0.3)
    print(f"Mouse moved to ({new_x}, {new_y}) due to inactivity")

while True:
    current_pos = pyautogui.position()

    if current_pos != last_mouse_pos:
        last_mouse_pos = current_pos
        last_movement_time = time.time()

    seconds_since_movement = time.time() - last_movement_time
    now = datetime.now(warsaw_tz).time()

    if seconds_since_movement >= 60 and dt_time(7, 2) <= now <= dt_time(22, 2):
        move_mouse_randomly()

        sleep_d = random.randint(5, 30)
        time.sleep(sleep_d)

        pyautogui.press('scrolllock')
        pyautogui.press('scrolllock')
        last_mouse_pos = pyautogui.position()
        last_movement_time = time.time()

        print("No activity during working hours. Actions performed at {}".format(datetime.now(warsaw_tz).time()))
    else:
        print(f"No action taken at {now} (active or outside working hours)")

    sleep_duration = random.randint(10, 180)
    print(f"Next check in {sleep_duration} seconds")
    time.sleep(sleep_duration)