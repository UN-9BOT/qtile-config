from libqtile import hook, qtile
from libqtile.command import lazy
import subprocess
import os
import re

def is_running(process):
    s = subprocess.Popen(["ps", "axw"], stdout=subprocess.PIPE)
    for x in s.stdout:
        if re.search(process, x.decode('utf-8')):
            return True
    return False


def execute_once(process):
    if not is_running(process):
        return subprocess.Popen(process.split())





@hook.subscribe.startup
def startup():
    execute_once("nm-applet")



@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

    
@hook.subscribe.startup_once
def _():
    # Set initial groups
    if len(qtile.screens) > 1:
        qtile.groups_map['w'].cmd_toscreen(0, toggle=False)
        qtile.groups_map['m'].cmd_toscreen(1, toggle=False)

@hook.subscribe.client_new
def client_new(client):
    if 'Brave' in str(client.name):
        client.togroup('w')
    if 'Sublime' in str(client.name):
        client.togroup('0')
    if 'PyCharm' in str(client.name):
        client.togroup('c')
    if 'YaMusic' in str(client.name):
        client.togroup('m')
    if 'Volume Control' in str(client.name):
        client.togroup('m')
    if 'Telegram' in str(client.name):
        client.togroup('t')
    if 'Obsidian' in str(client.name):
        client.togroup('c')
    if 'btop' == str(client.name):
        client.togroup('m')

@hook.subscribe.client_new
def dialogs(window):
    if (window.window.get_wm_type() == 'dialog'
            or window.window.get_wm_transient_for()):
        window.floating = True


# @hook.subscribe.client_new
# def vue_tools(window):
#     if((window.window.get_wm_class() == (
#         'sun-awt-X11-XWindowPeer', 'tufts-vue-VUE')
#             and window.window.get_wm_hints()['window_group'] != 0)
#             or (window.window.get_wm_class() == (
#                 'sun-awt-X11-XDialogPeer', 'tufts-vue-VUE'))):
#         window.floating = True


# @hook.subscribe.client_new
# def idle_dialogues(window):
#     if((window.window.get_name() == 'Search Dialog') or
#       (window.window.get_name() == 'Module') or
#       (window.window.get_name() == 'Goto') or
#       (window.window.get_name() == 'IDLE Preferences')):
#         window.floating = True


# @hook.subscribe.client_new
# def libreoffice_dialogues(window):
#     if ((window.window.get_wm_class() == (
#         'VCLSalFrame', 'libreoffice-calc')) or
#             (window.window.get_wm_class() == (
#                 'VCLSalFrame', 'LibreOffice 3.4'))):
#         window.floating = True
