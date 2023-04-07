# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os.path

from libqtile import bar, layout, widget, hook

from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import subprocess

win = "mod4"
alt = "mod1"
numlock = "mod2"
mod = win
strg = "control"

terminal = guess_terminal()


@hook.subscribe.startup_once
def autostart_once():
    try:
        subprocess.Popen(["python", os.path.expanduser("~/.config/qtile/wallpaper_change.py")])
    except Exception:
        pass


@hook.subscribe.startup
def autostart():
    import locate_config_files
    locate_config_files.cp_there()
    shell_processes = [
        # "feh --bg-fill /home/bergschaf/.config/qtile/wallpapers/Metall SGS.png",
        "picom --config ~/.config/qtile/picom-blur.conf",
        "xmodmap ~/.config/qtile/.xmodmap",
    ]
    processes = [
        ["xrandr", "--output", "DP-0", "--off", "--output", "DP-1", "--off", "--output", "DP-2", "--off", "--output",
         "DP-3", "--mode", "1680x1050", "--pos", "2560x195", "--rotate", "normal", "--output", "HDMI-0", "--off",
         "--output", "DP-4", "--mode", "2560x1440", "--pos", "0x0", "--rotate", "normal", "--output", "DP-5", "--off"],

    ]
    for p in shell_processes:
        subprocess.Popen(p, shell=True)
    for p in processes:
        subprocess.Popen(p)


keys = [
    # media playpause str alt shift p
    Key([strg, alt, "shift"], "p", lazy.spawn("playerctl play-pause"), desc="Playpause"),
    # media next str alt shift s
    Key([strg, alt, "shift"], "s", lazy.spawn("playerctl next"), desc="Next"),

    # launch rofi
    Key([alt], "r", lazy.spawn("rofi -show drun"), desc="Launch rofi"),
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([alt], "j", lazy.layout.left(), desc="Move focus to left"),
    Key([alt], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([alt], "k", lazy.layout.down(), desc="Move focus down"),
    Key([alt], "i", lazy.layout.up(), desc="Move focus up"),
    # Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Switch between screens
    Key([alt], "u", lazy.to_screen(1), desc="Keyboard focus to monitor 1"),
    Key([alt], "o", lazy.to_screen(0), desc="Keyboard focus to monitor 2"),
    # Key([alt], "space", lazy.next_screen(), desc="Move focus to next monitor"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([alt], "a", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([alt], "d", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([alt], "s", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([alt], "w", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction

    # will be to screen edge - window would shrink.
    Key([alt, "shift"], "a", lazy.layout.grow_left(), desc="Grow window to the lleft"),
    Key([alt, "shift"], "d", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([alt, "shift"], "s", lazy.layout.grow_down(), desc="Grow window down"),
    Key([alt, "shift"], "w", lazy.layout.grow_up(), desc="Grow window up"),

    Key([alt, "control"], "a", lazy.layout.shrink_left(), desc="Shrink window to the lleft"),
    Key([alt, "control"], "d", lazy.layout.shrink_right(), desc="Shrink window to the right"),
    Key([alt, "control"], "s", lazy.layout.shrink_down(), desc="Shrink window down"),
    Key([alt, "control"], "w", lazy.layout.shrink_up(), desc="Shrink window up"),

    # move between workspaces when pressing

    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes

    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([alt], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([win], "l", lazy.spawn("slock"), desc="Lock the screen"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]
groups = [Group("1", spawn="discord"), Group("2", spawn="spotify")]
groups.extend([Group(i) for i in "3456789"])

# cycle to groups with alt + shift + D and alt + shift + A
Key([alt, "shift"], "d", lazy.screen.next_group(), desc="Move to next group"),
Key([alt, "shift"], "a", lazy.screen.prev_group(), desc="Move to previous group"),

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [alt],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [alt, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=2, margin=5),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="liberation mono",
    fontsize=16,
    padding=7,
)
extension_defaults = widget_defaults.copy()

screens = [

    Screen(
        left=bar.Gap(10),
        right=bar.Gap(10),
        bottom=bar.Gap(10),
        top=
        bar.Bar(
            [
                # widget.Sep(padding=20, linewidth=5, foreground="ffffff"),
                widget.TextBox(" ", padding=10),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Systray(),
                widget.Clock(padding=30),

                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                # widget.Systray(),

            ],
            30,
            # padding above and below the bar
            margin=[10, 10, 10, 10],  #
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # wallpaper="~/Pictures/garuda-wallpapers/src/garuda-wallpapers/Shani.png",
        # wallpaper_mode="fill"
    ),
    Screen(
        left=bar.Gap(10),
        right=bar.Gap(10),
        bottom=bar.Gap(10),
        top=bar.Bar(
            [
                # widget.Sep(padding=20, linewidth=5, foreground="ffffff"),
                # spacer
                widget.TextBox(" ", padding=10),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Systray(),
                widget.Clock(padding=30),

                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                # widget.Systray(),

            ],
            30,
            margin=[10, 10, 10, 10],  #

            #    border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            #    border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # wallpaper="~/Pictures/garuda-wallpapers/src/garuda-wallpapers/Darkwing Beast.jpg",
        # wallpaper_mode="fill"
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
