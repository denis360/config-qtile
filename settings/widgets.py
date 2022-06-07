from libqtile import widget
from .loadtheme import colors

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

def desktops_workspaces():
    return [
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
                this_current_screen_border=colors["focus"],
                this_screen_border=colors["grey"],
                other_current_screen_border=colors["color1"],
                other_screen_border=colors["grey"]
            ),

        widget.Spacer(background=colors["dark"]),

    ]

widgets_screen_central = [
    *desktops_workspaces(),

    powerline(colors["dark"], colors["dark"]),
    widget.Systray(background=colors["dark"]),
    icon(colors["dark"], colors["dark"], " ", 3),

    powerline(colors["color4"], colors["dark"]),
    widget.CurrentLayoutIcon(background=colors["color4"], scale=0.5),
    widget.CurrentLayout(background=colors["color4"],foreground=colors["text"]),

    powerline(colors["color2"], colors["color4"]),
    icon(colors["text"], colors["color2"], "", 20),
    widget.Memory(background=colors["color2"], foreground=colors["text"], format='{MemUsed:.0f}{mm} '),

    powerline(colors["color3"], colors["color2"]),
    icon(colors["text"], colors["color3"], "", 20),
    widget.Clock(background=colors["color3"], foreground=colors["text"], format='%d/%m '),
    widget.Clock(background=colors["color3"], foreground=colors["text"], format='- %H:%M '),
]

others_screens = [
    *desktops_workspaces(),

    powerline(colors["color4"], colors["dark"]),
    widget.CurrentLayoutIcon(background=colors["color4"], scale=0.5),
    widget.CurrentLayout(background=colors["color4"],foreground=colors["text"]),
]

widget_defaults = {
    'font': 'CaskaydiaCove NF Bold',
    'fontsize': 13,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()

