import os
import random
import subprocess

WALLPAPER_DIR = os.path.expanduser("~/.config/qtile/wallpapers")

def set_random_wallpaper():
    wallpapers = os.listdir(WALLPAPER_DIR)
    wallpaper = random.choice(wallpapers)
    subprocess.call(["feh", "--bg-fill", os.path.join(WALLPAPER_DIR, wallpaper)])


set_random_wallpaper()