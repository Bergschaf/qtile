import os.path
import subprocess

PKGLIST_IMPORTANT = os.path.expanduser("~/.config/qtile/pkglist_important.txt")
PKGLIST = os.path.expanduser("~/.config/qtile/pkglist.txt")

COMMAND_IMPORTANT = "sudo pacman -S --needed - < " + PKGLIST_IMPORTANT
COMMAND_ALL = "sudo pacman -S --needed - < " + PKGLIST
if __name__ == '__main__':
    # parse console arguments, if -i is passed, install only important packages
    # if -a is passed, install all packages
    # if no arguments are passed, install all packages
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--important", help="install only important packages", action="store_true")
    parser.add_argument("-a", "--all", help="install all packages", action="store_true")
    args = parser.parse_args()
    subprocess.run(COMMAND_IMPORTANT, shell=True)
    # transparent lockscreen
    subprocess.run("betterlockscreen -u . --fx color --color #000000", shell=True)
    if not args.important:
        subprocess.run(COMMAND_ALL, shell=True)
