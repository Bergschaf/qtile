import os

CONFIG_DIR = "~/.config/qtile/configs"
config_dirs = ["alacritty", "fish", "starship", "rofi", "conky", "dunst"]
config = [
    ("alacritty.yml", "~/.config/alacritty/alacritty.yml"),
    ("config.fish", "~/.config/fish/config.fish"),
    ("starship.toml", "~/.config/starship.toml"),
    ("config.rasi", "~/.config/rofi/config.rasi"),
    ("conky.conf", "~/.config/conky/conky.conf"),
]


def check_dirs():
    for dir in config_dirs:
        if not os.path.isdir(os.path.join(CONFIG_DIR, dir)):
            print(f"Creating directory: {dir}")
            os.mkdir(os.path.join(CONFIG_DIR, dir))


def cp_here():
    input("Do you want to copy the config files to the current directory and overwrite them? (y/n) ")
    # backup config dir
    os.system(f"cp -r {CONFIG_DIR} {CONFIG_DIR}_backup")

    for file in config:
        os.system(f"cp {file[1]} {os.path.join(CONFIG_DIR, file[0])}")

    print("Done!")


def cp_there():
    check_dirs()
    for file in config:
        os.system(f"cp {os.path.join(CONFIG_DIR, file[0])} {file[1]}")


if __name__ == '__main__':
    cp_there()
    # cp_here()
