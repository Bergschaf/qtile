import os
import random
import subprocess
import time

WALLPAPER_DIR = os.path.expanduser("~/.config/qtile/wallpapers")
WALLPAPER_CHANGE_MIN = 10

def set_random_wallpaper():
    wallpapers = os.listdir(WALLPAPER_DIR)
    wallpaper = random.choice(wallpapers)
    subprocess.call(["feh", "--bg-fill", os.path.join(WALLPAPER_DIR, wallpaper)])

def start_timer():
    time.sleep(2)
    while True:
        set_random_wallpaper()
        time.sleep(WALLPAPER_CHANGE_MIN * 60)

start_timer()