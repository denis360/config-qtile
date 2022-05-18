from typing import List

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import json
from os import path

qtile_path = path.join(path.expanduser('~'), ".config", "qtile")

with open(path.join(qtile_path, "config-theme.json"), "r") as t:
    theme = json.load(t)["theme"]

with open(path.join(qtile_path, "themes", f"{theme}.json")) as f:
    colors = json.load(f)

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.shrink(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Brightness control
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 10%+")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    # or use keyboard shortcuts
    Key([mod, "shift"], "Up", lazy.spawn("brightnessctl set 10%+")),
    Key([mod, "shift"], "Down", lazy.spawn("brightnessctl set 10%-")),

    # Volume control
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master 5%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master 5%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer sset Master toggle")),
    # or use keyboard shortcuts
    Key([mod, "control"], "Up", lazy.spawn("amixer sset Master 5%+")),
    Key([mod, "control"], "Down", lazy.spawn("amixer sset Master 5%-")),
    Key([mod, "control"], "m", lazy.spawn("amixer sset Master toggle")),

    # App shortcuts
    Key([mod], "b", lazy.spawn("google-chrome-stable --force-device-scale-factor=0.9")),
    # Screenshots
    Key([mod], "s", lazy.spawn("scrot Screenshot_%Y-%m-%d_%H-%M-%S.png --pointer -d 2 -e 'mv $f ~/Pictures/'")),
    Key([mod, "shift"], "s", lazy.spawn("scrot Screenshot_%Y-%m-%d_%H-%M-%S.png -s -d 2 -e 'mv $f ~/Pictures/'")),
    Key([mod], "space", lazy.spawn("dmenu_run")),
    Key([mod, "shift"], "space", lazy.spawn("dmenu_run")),
]

# WorkSpaces
groups = [Group(i) for i in [
    "", "", "", "", "", "", "", "", ""
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

layouts = [
    layout.Max(),
    layout.MonadTall(
        border_focus=colors["color2"],
        border_width=2,
        margin=5
        ),
    layout.MonadWide(
        border_focus=colors["color2"],
        border_width=2,
        margin=5
        ),
    # layout.VerticalTile(),
    # layout.Columns(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.Zoomy(),
]

widget_defaults = {
    'font': 'CaskaydiaCove NF Bold',
    'fontsize': 13,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()



def powerline(fg="#000000", bg="#000000"):
    return widget.TextBox(
            text="",
            background=bg,
            foreground=fg,
            padding=-5,
            fontsize=40
            )

def icon(fg=colors["dark"], bg="#000000", text="?", fsize=13):
    return widget.TextBox(
            text=text,
            background=bg,
            foreground=fg,
            fontsize=fsize
            )



screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    fontsize=25,
                    inactive=colors["inactive"],
                    active=colors["active"],
                    padding_y=5,
                    padding_x=12,
                    margin_x=4,
                    rounded=False,
                    background=colors["dark"],
                    foreground=colors["light"],
                    borderwidth=1,
                    highlight_method="block",
                    this_current_screen_border=colors["color2"],
                    this_screen_border=colors["grey"],
                    other_current_screen_border=colors["color3"],
                    other_screen_border=colors["grey"]
                    ),

                widget.Spacer(background=colors["dark"]),

                powerline(colors["color3"], colors["dark"]),
                widget.CurrentLayoutIcon(background=colors["color3"], scale=0.60),
                widget.CurrentLayout(background=colors["color3"],foreground=colors["text"]),

                powerline(colors["color2"], colors["color3"]),
                icon(colors["text"], colors["color2"], "", 20),
                widget.Memory(background=colors["color2"], foreground=colors["text"], format='{MemUsed:.0f}{mm} '),

                powerline(colors["color4"], colors["color2"]),
                icon(colors["text"], colors["color4"], "", 20),
                widget.Clock(background=colors["color4"], foreground=colors["text"], format='%d/%m'),
                icon(colors["text"], colors["color4"], " ", 20),
                widget.Clock(background=colors["color4"], foreground=colors["text"], format='%H:%M '),

                powerline(colors["dark"], colors["color4"]),
                widget.Systray(background=colors["dark"]),
                icon(colors["dark"], colors["dark"], " ", 20),
            ],
            23, opacity=0.93
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    fontsize=25,
                    inactive=colors["inactive"],
                    active=colors["active"],
                    padding_y=5,
                    padding_x=12,
                    margin_x=4,
                    rounded=False,
                    background=colors["dark"],
                    foreground=colors["light"],
                    borderwidth=1,
                    highlight_method="block",
                    this_current_screen_border=colors["color2"],
                    this_screen_border=colors["grey"],
                    other_current_screen_border=colors["color3"],
                    other_screen_border=colors["grey"]
                    ),

                widget.Spacer(background=colors["dark"]),

                powerline(colors["color4"], colors["dark"]),
                icon(colors["text"], colors["color4"], "", 20),
                widget.Clock(background=colors["color4"], foreground=colors["text"], format='%d/%m'),
                icon(colors["text"], colors["color4"], " ", 20),
                widget.Clock(background=colors["color4"], foreground=colors["text"], format='%H:%M   '),
            ],
            23, opacity=0.93
        )
    )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),
    Match(wm_class='makebranch'),
    Match(wm_class='maketag'),
    Match(wm_class='ssh-askpass'),
    Match(title='branchdialog'),
    Match(title='pinentry'),
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wmname = "Qtile"

