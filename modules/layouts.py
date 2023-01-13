from libqtile import layout
from libqtile.config import Match

border_focus='#e78284'
border_normal='#f2d5cf'
margin = 4
margin_on_single = 6
cr = 5
bw = 4



layout_theme = {
    "border_width": 2,
    "margin": margin,
    "border_focus": "e1acff",
    "border_normal": border_normal,
}


layouts = [
    # layout.MonadTall(margin=5, border_focus='#e78284',
    #                  border_normal='#f2d5cf', margin_on_single=3, border_width=4),
    # layout.Columns(border_focus_stack='#d75f5f'),
    
    # layout.Floating(**layout_theme),
    layout.Columns(
        insert_position=1,
        border_width=bw,
        border_focus=border_focus,
        border_normal=border_normal,
        border_on_single=True,
        wrap_focus_columns=False,
        wrap_focus_rows=False,
        margin=margin,
        margin_on_single=margin_on_single,
        corner_radius=cr,
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Spiral(),
    # layout.Zoomy(columnwidth=200, margin=4),
]

# floating_layout = layout.Floating(float_rules=[
#     # Run the utility of `xprop` to see the wm class and name of an X client.
#     *layout.Floating.default_float_rules,
#     Match(wm_class='confirmreset'),  # gitk
#     Match(wm_class='makebranch'),  # gitk
#     Match(wm_class='maketag'),  # gitk
#     Match(wm_class='ssh-askpass'),  # ssh-askpass
#     Match(title='branchdialog'),  # gitk
#     Match(title='pinentry'),  # GPG key password entry
# ])

floating_layout = layout.Floating(
    border_width=bw,
    border_focus=border_focus,
    border_normal=border_normal,
    corner_radius=cr,
    float_rules=[
        Match(title='Open File'),
        Match(title='Media viewer'),
        Match(title='Unlock Database - KeePassXC'),  # Wayland
        Match(title='File Operation Progress', wm_class='thunar'),  # Wayland
        Match(wm_class='Arandr'),
        Match(wm_class='org.kde.ark'),
        Match(wm_class='confirm'),
        Match(wm_class='dialog'),
        Match(wm_class='download'),
        Match(wm_class='error'),
        Match(wm_class='fiji-Main'),
        Match(wm_class='file_progress'),
        Match(wm_class='imv'),
        Match(wm_class='lxappearance'),
        Match(wm_class='mpv'),
        Match(wm_class='notification'),
        # Match(wm_class='pavucontrol'),
        Match(wm_class='Pinentry-gtk-2'),
        Match(wm_class='qt5ct'),
        Match(wm_class='ssh-askpass'),
        Match(wm_class='Dragon'),
        Match(wm_class='Dragon-drag-and-drop'),
        Match(wm_class='toolbar'),
        Match(wm_class='wlroots'),
        Match(wm_class='Xephyr'),
        Match(wm_type='dialog'),
        Match(role='gimp-file-export'),
        Match(func=lambda c: c.has_fixed_size()),
        Match(func=lambda c: bool(c.is_transient_for())),
    ]
)