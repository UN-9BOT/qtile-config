from libqtile import qtile
from modules.widgets_custom import volumes, tasklist


colors = [
    ["#282c34", "#282c34"],  # panel background
    ["#3d3f4b", "#434758"],  # background for current screen tab
    ["#ffffff", "#ffffff"],  # font color for group names
    ["#ff5555", "#ff5555"],  # border line color for current tab
    ["#74438f", "#74438f"],  # border line color for 'other tabs' and color for 'odd widgets'
    ["#4f76c7", "#4f76c7"],  # color for the 'even widgets'
    ["#e1acff", "#e1acff"],  # window name
    ["#ecbbfb", "#ecbbfb"]  # backbround for inactive screens
]

widget_defaults = dict(
    font='Terminus', # Cantarell
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()


volume = volumes.MyVolume(
    fontsize=18,
    # Font Awesome 5 Free
    font='Terminus',
    foreground=colors[4],
    background='#2f343f',
    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("pavucontrol")}
)

tasklist = tasklist.TaskList()