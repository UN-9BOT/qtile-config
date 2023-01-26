#!/bin/sh

## mode monitor
xrandr --output HDMI-A-0 --mode 1920x1080 --rate 74.97 --pos 0x0 --primary
xrandr --output eDP --mode 1920x1080 --pos 1920x0


## set US key
setxkbmap -layout us,ru
feh --bg-scale /home/un9bot/.config/qtile/walls/flatppuccin_4k_macchiato.png   # wallaper
picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

## Low battery notifier
~/.config/qtile/scripts/check_battery.sh & disowne

## Start welcome
# eos-welcome & disown

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME



## start apps

subl & disown
gtk-launch YaMusic.desktop & disown
terminology -T=btop -e btop & disown
telegram-desktop & disown
diodon & disown
# pycharm & disown
yandex-disk-indicator & disown
brave & disown
kdeconnect-cli -n un9droid --pair & disown
kdeconnect-indicator & disown
crow & disown
# obsidian & disown
udiskie -a  -n -t & disown
pavucontrol & disown


## start services
systemctl start bluetooth.service



## ntfy
curl \
  -H "Title: Start MSI" \
  -H "Priority: urgent" \
  -H "Tags: warning,skull" \
  -d "" \
  ntfy.sh/21sch_un \
  & disown
