import subprocess

packages = \
["swaybg", #Основные пакеты!
"foot",
"waybar",
"fish",
"rofi",
"nwg-look",
"hyprlock",
"gtk2",
"gtk3",
"w3m",
"sddm",
"qt5",
"mako",

#Шрифты !

"ttf-jetbrains-mono",
"breeze",

#Утилиты

"inetutils",
"pkgfile",
"base-devel",
"grim",
"catppuccin",

#Обновления

"sudo pacman -Syu"

]


for packag in  packages:
    subprocess.run(["sudo", "pacman", "-S", "--noconfirm", packag])
