from libqtile.config import Key, Group, Match
from libqtile.command import lazy
from libqtile import layout
from .keys import keys, mod

# groups = [Group(i) for i in ['1', '2', '3', '4', 'w', 'c', 't', '0', 'm']]
# groups = [Group("1"), Group("2"), Group("3", matches=[Match(wm_class="Mozilla Firefox")])]
groups = [
    Group('1'),
    Group('2'),
    Group('3'),
    Group('4'),
    Group('w'),
    Group('c'),
    Group('t'),
    Group('0'),
    Group('m', layout = "matrix"),
    ]

# def _go_to_group(name: str):
#     """
#     This creates lazy functions that jump to a given group. When there is more than one
#     screen, the first 3 and second 3 groups are kept on the first and second screen.
#     E.g. going to the fourth group when the first group (and first screen) is focussed
#     will also change the screen to the second screen.
#     """
#     def _inner(qtile) -> None:
#         if len(qtile.screens) == 1:
#             qtile.groups_map[name].cmd_toscreen()
#             return

#         old = qtile.current_screen.group.name
#         if name in '123':
#             qtile.focus_screen(0)
#             if old in '1234' or qtile.current_screen.group.name != name:
#                 qtile.groups_map[name].cmd_toscreen()
#         else:
#             qtile.focus_screen(1)
#             if old in 'wct0m' or qtile.current_screen.group.name != name:
#                 qtile.groups_map[name].cmd_toscreen()

#     return _inner


for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod],
            i.name,
            lazy.group[i.name].toscreen(),
            # lazy.function(_go_to_group(i.name)),
            desc="Switch to group {}".format(i.name)),

        Key([mod], "Right", lazy.screen.next_group(),
            desc="Switch to next group"),

        Key([mod], "Left", lazy.screen.prev_group(),
            desc="Switch to previous group"),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"],
            i.name,
            lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

