#!/bin/bash
# Steam Input Disabler installer
# Author: markurei

echo "Accessing working directory..."
if mkdir -p "$HOME/.steam_input_disabler" && cd $_ ; then
    pwd
else
    echo "Failed to create or access directory"
    exit 1
fi

echo "Checking version..."
wget --tries=3 -q https://github.com/markurei/steam-input-disabler/releases/download/latest/csum.md5

if [ ! -f "./csum.md5" ] ; then
    echo "Checksum download failed! Please try again"
    exit 1
else
    if [ -f "./app" ] ; then
        md5sum -b app > csum_current.md5
        if cmp -s csum.md5 csum_current.md5 ; then
            echo "Version already installed!"
            rm -rf csum*
            exit 1
        else
            rm -rf csum*
            echo "Creating backup..."
            mv app app_backup
        fi
    fi
fi

echo "Downloading:"
wget --tries=3 -q --show-progress https://github.com/markurei/steam-input-disabler/releases/download/latest/app

if [ ! -f "./app" ] ; then
    echo "Download failed!"
    if [ -f "./app_backup" ] ; then
        echo "Restoring backup..."
        mv app_backup app
    fi
    echo "Please check your internet connection and try again!"
    exit 1
fi

echo "Download complete!"

chmod +x app
rm app_backup &>/dev/null 

echo "Creating desktop shortcuts..."

# create app shortcut
rm "$HOME/Desktop/steam_input_disabler.desktop" &>/dev/null
echo '#!/usr/bin/env xdg-open
[Desktop Entry]
Name=Steam Input Disabler
Exec=cd $HOME/.steam_input_disabler; ./app
Icon=bittorrent-sync
Terminal=false
Type=Application
StartupNotify=false' > "$HOME/Desktop/steam_input_disabler.desktop"
chmod +x "$HOME/Desktop/steam_input_disabler.desktop"

# create uninstall shortcut
rm "$HOME/Desktop/uninstall_sid.desktop" &>/dev/null
echo '#!/usr/bin/env xdg-open
[Desktop Entry]
Name=Uninstall Steam Input Disabler
Exec=rm -rf "$HOME/.steam_input_disabler"; rm "$HOME/Desktop/steam_input_disabler.desktop"; rm "$HOME/Desktop/uninstall_sid.desktop"
Icon=delete
Terminal=false
Type=Application
StartupNotify=false' > "$HOME/Desktop/uninstall_sid.desktop"
chmod +x "$HOME/Desktop/uninstall_sid.desktop"

echo "Installation completed successfully!"

