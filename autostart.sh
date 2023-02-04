#!/bin/sh

## mode monitor
xrandr --output HDMI-A-0 --mode 1920x1080 --rate 74.97 --pos 0x0 --primary
xrandr --output eDP --mode 1920x1080 --pos 1920x0


## set US key
setxkbmap -layout us,ru
feh --bg-scale /home/un9bot/.config/qtile/walls/flatppuccin_4k_macchiato.png   # wallaper
picom &  # --experimental-backends --vsync should prevent screen tearing on most setups if needed

## Low battery notifier
~/.config/qtile/scripts/check_battery.sh & 


/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &  # start polkit agent from GNOME

## start apps
input-remapper-control --command stop-all && input-remapper-control --command autoload &
subl & 
/usr/lib/brave-bin/brave --profile-directory=Default --app-id=lhkhbcnmnacfgkhmincmdinafnopbgln & 
terminology -T=btop -e btop & 
telegram-desktop & 
diodon & 
# pycharm & 
yandex-disk-indicator & 
brave & 
kdeconnect-cli -n un9droid --pair & 
kdeconnect-indicator & 
crow & 
# obsidian & 
udiskie -a  -n -t & 
pavucontrol & 


## start services
systemctl start bluetooth.service



## ntfy
curl \
  -H "Title: Start MSI" \
  -H "Priority: urgent" \
  -H "Tags: warning,skull" \
  -d "" \
  ntfy.sh/21sch_un \
  & 
# disown