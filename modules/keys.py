from libqtile.lazy import lazy
from libqtile.config import Key

mod = "mod4"
terminal = "terminology"

keys = [
    # custom apps
    Key([mod], "e", lazy.spawn("thunar")),
    Key([], "Print", lazy.spawn("flameshot gui")),
    Key(["control", "mod1"], "v", lazy.spawn("diodon")),
    Key([mod], "F1", lazy.spawn("slock")),
    

    # Switch screens
    Key([mod], "v", lazy.to_screen(0)),
    Key([mod], "b", lazy.to_screen(1)),

    # Switch keyboard layouts
    Key([], "Scroll_Lock", lazy.spawn("setxkbmap -layout us,ru"), desc="Change to US layout"),
    Key(["shift"], "Scroll_Lock", lazy.spawn("setxkbmap -layout ru,us"), desc="Change to RU layout"),
    # Key([mod], "F12", lazy.spawn("setxkbmap ru"), desc="Change to RU layout"),
    # Key([mod], "F11", lazy.spawn("setxkbmap us"), desc="Change to US layout"),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod],
        "Tab",
        lazy.layout.next(),
        desc="Move window focus to other window"),

    Key([mod], "z", lazy.spawn("rofi -show drun"), desc="spawn rofi"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], 
        "k", 
        lazy.layout.shuffle_up(), 
        desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    # Key([mod, "control"],
    #     "h",
    #     lazy.layout.swap_left(),
    #     desc="Grow window to the left"),
    # Key([mod, "control"],
    #     "l",
    #     lazy.layout.grow_right(),
    #     desc="Grow window to the right"),
    Key([mod, "control"],
        "j",
        lazy.layout.shrink(),
        desc="Grow window down"),
    Key([mod, "control"], 
        "k", 
        lazy.layout.grow(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "shift"], "space", lazy.layout.flip(), desc="Flip main window on other side"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"],
        "z",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 3%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 3%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),
]
