import json
from os import path
from .path import qtile_path

def load_theme ():
    loaded_theme = path.join(qtile_path, "config-theme.json")
    with open(path.join(loaded_theme)) as t:
        theme = json.load(t)["theme"]

    with open(path.join(qtile_path, "themes", f"{theme}.json")) as f:
        print(loaded_theme)
        return json.load(f)


if __name__ == "settings.loadtheme":
    colors = load_theme()

