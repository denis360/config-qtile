from libqtile.config import Key, Click, Drag
from libqtile.command import lazy

mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),
    ([mod, "shift"], "f", lazy.window.toggle_floating()),
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    ([mod], "w", lazy.window.kill()),

    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    ([mod, "control"], "r", lazy.restart()),
    ([mod, "control"], "q", lazy.shutdown()),

    # ------------ App Configs ------------

    ([mod], "space", lazy.spawn("rofi -show drun")),
    ([mod, "shift"], "space", lazy.spawn("rofi -show run")),
    ([mod], "b", lazy.spawn("google-chrome-stable --force-device-scale-factor=0.8")),
    ([mod], "e", lazy.spawn("thunar")),
    ([mod], "g", lazy.spawn("geeqie")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),

    ([mod], "r", lazy.spawn("redshift -O 8000")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    ([mod], "s", lazy.spawn("scrot Screenshot_%Y-%m-%d_%H-%M-%S.png --pointer -d 2 -e 'mv $f ~/Pictures/screenshots'")),
    ([mod, "shift"], "s", lazy.spawn("scrot Screenshot_%Y-%m-%d_%H-%M-%S.png -s -d 2 -e 'mv $f ~/Pictures/screenshots'")),

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    ([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    ([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    # Volume shortcuts
    ([mod, "control"], "Down", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    ([mod, "control"], "Up", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    ([mod, "control"], "m", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    # Brightness
    ([mod, "shift"], "Up", lazy.spawn("brightnessctl set +5%")),
    ([mod, "shift"], "Down", lazy.spawn("brightnessctl set 5%-")),
]]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]


