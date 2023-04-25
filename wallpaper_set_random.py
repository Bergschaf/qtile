import os
import random
import subprocess
import time

WALLPAPER_DIR = os.path.expanduser("~/.config/qtile/wallpapers")


def set_random_wallpaper():
    wallpapers = os.listdir(WALLPAPER_DIR)
    wallpaper = random.choice(wallpapers)
    subprocess.call(["feh", "--bg-fill", os.path.join(WALLPAPER_DIR, wallpaper)])


set_random_wallpaper()

if __name__ == '__main__':
    wallpaper = "/home/bergschaf/.config/qtile/wallpapers/Circuit.png"
    # load the wallpaper into RAM to acces it faster

