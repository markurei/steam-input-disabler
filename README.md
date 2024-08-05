
# Steam Input Disabler

A utility to conveniently disable or enable Steam input for all non-Steam games added via Lutris, HeroicLauncher, etc. in the Steamdeck.

## Description

Some games, specially ones that are added as non-Steam games, have issues regarding Steamdeck controls not being detected properly. Keyboard controls will be used intead, making the Steamdeck controls unusable.
The immediate workaround for this is to map mouse and keyboard keys to the controls in Steamdeck but the game itself would still display keyboard controls in-game.

Disabling the Steam input for that specific game fixes the issue. While it can be done manually, this application handles it automatically. This application disables or enables the Steam input setting from the Steam config itself fixing the controller and in-game controller prompts/display issues for non-Steam games.

> [!NOTE]
> Steam games does not have this issue since the user can disable Steam Input from the Steam UI directly.
> Non-Steam games does not show this option in the Steam UI for Steamdeck.

  
> [!WARNING]
> This application was tested only on Steamdeck running SteamOS.
> It may or may NOT work on other Linux distros.
> Does not work on Windows.

  

## Getting Started

### Download

<h1  align="center">
		Steam Input Disabler
		<br>
	<a  name="download button"  href="https://raw.githubusercontent.com/markurei/steam-input-disabler/main/install_SteamInputDisabler.desktop">
	<img  src="https://raw.githubusercontent.com/markurei/steam-input-disabler/main/images/download_banner.svg"  alt="Download"  width="250px"  style="padding-top: 15px;"></a>
</h1>

### Installation

Make sure your Steamdeck has a stable network connection and available storage.
1. If in Game Mode, press the Steam button and go to Power -> Switch to Desktop.
2. Once in the desktop, go to this Github page on your preferred browser.
3. Download the file linked above. If it does not automatically download, right-click the link and choose **'Save link as'**.
4. If the downloaded file is named `install_SteamInputDisabler.desktop.download`, rename it to `install_SteamInputDisabler.desktop` before proceeding to below steps.
5. Drag the file onto your desktop first and double-click to execute it.

### Using the application

After installation is completed, a desktop shortcut named `Steam Input Disabler` should appear.
1.  <font  color="red">**Important**</font>. Quit or exit Steam first before running the application. Cannot save new settings when Steam is still running.
2. Double-click on the shortcut to run the app.
3. Set the filter dropdown button to either Lutris (<em>default</em>), HeroicLauncher, or All Non-Steam.
4. Click the toggle button to set the Steam input per game.
<svg  xmlns="http://www.w3.org/2000/svg"  viewBox="0 0 576 512"  width="50px"  height="30px"  fill="#3d85c6"  ><!--!Font Awesome Free 6.6.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path  d="M192 64C86 64 0 150 0 256S86 448 192 448l192 0c106 0 192-86 192-192s-86-192-192-192L192 64zm192 96a96 96 0 1 1 0 192 96 96 0 1 1 0-192z"/></svg> = Enabled
<svg  xmlns="http://www.w3.org/2000/svg"  viewBox="0 0 576 512"  width="50px"  height="30px"  fill="#808080"><!--!Font Awesome Free 6.6.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path  d="M384 128c70.7 0 128 57.3 128 128s-57.3 128-128 128l-192 0c-70.7 0-128-57.3-128-128s57.3-128 128-128l192 0zM576 256c0-106-86-192-192-192L192 64C86 64 0 150 0 256S86 448 192 448l192 0c106 0 192-86 192-192zM192 352a96 96 0 1 0 0-192 96 96 0 1 0 0 192z"/></svg> = Disabled
5. Click save after setting the values and close the application.
6. Start Steam or go back to Game Mode and run the game to check the controls.


### Uninstallation

For clean uninstallation, please follow below steps.

1. If in Game Mode, press the Steam button and go to Power -> Switch to Desktop.
2. Double-click on the `Uninstall Steam Input Disabler` shortcut to remove the files.
3. If that shortcut is not available, then open File Manager and delete the folder below:
```
/home/deck/.steam_input_disabler
```

### Dependencies

Created using
* Python 3.11 (or above) with tkinter enabled/added
* Ubuntu 22.04

Used modules
* pyinstaller
* vdf
* customtkinter
* CTkMessagebox

### Build binary manually

Prepare a Linux environment with Python and tkinter installed and all module dependencies installed using `pip`.
1. Execute below command in a Linux environment terminal:
```
pyinstaller --noconsole --onefile app.py --hidden-import='PIL._tkinter_finder'
```

## Authors

Contributors and contact info

👤 **markurei**

* Github: [@markurei](https://github.com/markurei)
* Youtube: [@deckoftrades](https://www.youtube.com/@deckoftrades)
* Email: deckofalltrades@gmail.com

## Version History

🆕 1.0

* Initial Release

  
## License

This project is licensed under the [MIT License](https://github.com/markurei/steam-input-disabler/LICENSE).


## Acknowledgments

This is a very basic Python applicationThis project is made possible by these awesome repos

* [pyinstaller](https://github.com/pyinstaller/pyinstaller)
* [customtkinter](https://github.com/TomSchimansky/CustomTkinter)
* [vdf](https://github.com/ValvePython/vdf)
* [CTkMessagebox](https://github.com/Akascape/CTkMessagebox)