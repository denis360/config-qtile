from libqtile.config import Screen
from libqtile import bar
from .widgets import widgets_screen_central, others_screens
from libqtile.log_utils import logger
import subprocess

def status_bar(widgets):
    return bar.Bar(widgets, 23, opacity=0.95)

screens = [Screen(top=status_bar(widgets_screen_central))]

xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"

command = subprocess.run(
    xrandr,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

if command.returncode != 0:
    er = command.stderr.decode("UTF-8")
    logger.error("Error to the count montors {0}:\n{1}".format(xrandr, er))
    monitors_up = 1
else:
    monitors_up = int(command.stdout.decode("UTF-8"))

if monitors_up > 1:
    for i in range(1, monitors_up):
        screens.append(Screen(top=status_bar(others_screens)))

