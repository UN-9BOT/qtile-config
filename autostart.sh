#!/bin/sh

## set US key
setxkbmap -layout us,ru
feh --bg-scale /home/un9bot/.config/qtile/walls/flatppuccin_4k_macchiato.png
picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

## Low battery notifier
~/.config/qtile/scripts/check_battery.sh & disowne

## Start welcome
# eos-welcome & disown

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME

## mode monitor
xrandr --output HDMI-A-0 --mode 1920x1080 --rate 74.97 --pos 0x0 --primary
xrandr --output eDP --mode 1920x1080 --pos 1920x0

## start apps
export TERM=terminology
export TERMINAL=terminology


subl & disown
telegram-desktop & disown
diodon & disown
pycharm & disown
yandex-disk-indicator & disown
brave & disown
gtk-launch YaMusic.desktop & disown
kdeconnect-cli -n un9droid --pair & disown
kdeconnect-indicator & disown
pavucontrol & disown
crow & disown
obsidian & disown



## start services
systemctl start bluetooth.service
