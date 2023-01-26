from modules.groups import groups
from modules.layouts import layouts, floating_layout
from modules.mouse import mouse
import os
from modules.screens import screens
from modules.keys import keys, mod
from modules.hooks import *


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
auto_minimize = True
focus_on_window_activation = "smart"
wmname = "Qtile"
reconfigure_screens = False 
widget_defaults = dict(
        font='Terminus',
        fontsize=13,
        padding=3
)