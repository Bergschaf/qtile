from wallpaper_set_random import set_random_wallpaper
import time

WALLPAPER_CHANGE_MIN = 10

def start_timer():
    time.sleep(2)
    while True:
        set_random_wallpaper()
        time.sleep(WALLPAPER_CHANGE_MIN * 60)

start_timer()