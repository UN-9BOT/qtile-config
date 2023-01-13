from libqtile.config import Click, Drag
from libqtile.lazy import lazy
from .keys import mod

# Drag floating layouts.
mouse = [
    Drag([mod, 'shift'], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod, 'shift'], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod, 'shift'], "Button1", lazy.window.bring_to_front())
]
