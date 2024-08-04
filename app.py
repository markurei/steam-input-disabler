import vdf
import os
from tkinter import *
import customtkinter
from CTkMessagebox import CTkMessagebox
import functools
from sys import exit

# config path
SHORTCUTS_VDF_PATH = "/config/shortcuts.vdf"
USERDATA_PATH = "/home/deck/.local/share/Steam/userdata/"
LOCALCONFIG_VDF_PATH = "/config/localconfig.vdf"

FILTER_ALL = "All Non-Steam"
FILTER_LUTRIS = "Lutris"
FILTER_HEROIC = "HeroicLauncher"

# filter keywords
LUTRIS_IDENTIFIER = "lutris:rungameid"
HEROIC_IDENTIFIER = "heroic://"

# app version
APP_VERSION = "1.0"
# app logo
ICON_DATA = """
   iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARzQklUCAgICHwIZIgAAAG7SURBVDhPpZK7SgNhEIXPaB
   RBwQ0Idl46C8EkGsEbRvABUtmqnZ1JZWksbbw0glWSytY8gRFvhZesb7A+wa6FChoznr1kjRov4Da7M//M9585s4J/PvK5XysxA4/tq1BNAxLz
   z9WEooCul6LETaex5wNAz8fTeNU8RIymwlQdtCArU5eF+nkI0LPkElTyYaPWDgi6A2ovQEsf1SyGZ6LLdYgH0IvYAKptleDmW7Q+p1GNFBjPcp
   QNmbnKeTXoXYEx0glj8gkd/XsSjVs+4DRJSbxB9Z5zDrhz+jnwVi3J9BX94Jdd4Wg1i+BuelKUaGLJB7izq1qUZdZl6slYjoXrjC2ZvhwM8/b1
   DvOrjB0xEtEvW2gApFh45MYEvHtlV5hXP28k5HuAu86HNtvfos7Rh3Iwxt8AXvHJmOPNKwhdV/s6w9y265dER41vFQSAsrcJwS79yfgKbkzGIz
   SxRBPTPwPOkjssdP/KY46QYjNX627GJckc11j+DcCfC3kCHAzvFwP32eyv0DOy7nqzNz0IN4GhrU1EOtcam38FeEpPk+rBexey6Jm3KPuw8bIf
   FQRGphCpWjJhWs1UvgEO97YRg4e0ZgAAAABJRU5ErkJggg==
"""

# get all games
def read_shortcuts():
   try:
      with open(USERDATA_PATH + str(id) + SHORTCUTS_VDF_PATH, "rb") as f:
         d = vdf.binary_loads(f.read())
         return d
   except:
      return None

# get current steam user
def get_current_user():
   try:
      temp = 0
      id = None
      for user_f in os.scandir(USERDATA_PATH):
         try:
            if user_f.is_dir():
               # get steam user ID from latest modified file
               time = os.path.getmtime(USERDATA_PATH + user_f.name + LOCALCONFIG_VDF_PATH)
               if time > temp:
                  temp = time
                  id = user_f.name
         except:
            pass
      return id
   except:
      return None

# get filtered games list
def filter_games(filter):
   games = []
   for x in shortcuts["shortcuts"]:
      if filter == FILTER_ALL:
         games.append(shortcuts["shortcuts"][x])
      elif filter == FILTER_LUTRIS:
         if LUTRIS_IDENTIFIER in shortcuts["shortcuts"][x]["LaunchOptions"]:
            games.append(shortcuts["shortcuts"][x])
      elif filter == HEROIC_IDENTIFIER:
         if HEROIC_IDENTIFIER in shortcuts["shortcuts"][x]["LaunchOptions"]:
            games.append(shortcuts["shortcuts"][x])
   return games

# get current steam user username
def get_user_name():
   try:
      d = vdf.parse(open(USERDATA_PATH + str(id) + LOCALCONFIG_VDF_PATH, encoding="utf8"))
      name = d["UserLocalConfigStore"]["friends"][id]["name"]
      return name
   except:
      return id

# check if steam process is running in background
def is_steam_running():
   try:
      ret = os.system("ps -e | grep -w steam")
      return ret
   except:
      return None

def display_scroll_frame(filter):
   games = filter_games(filter)

   global my_frame
   my_frame = customtkinter.CTkScrollableFrame(app,
      orientation="vertical",
      width=400,
      height=220,
      label_anchor = "center",
      corner_radius = 5)
   my_frame.columnconfigure(0, weight=1)
   my_frame.grid(row=1, column=0,columnspan=2, padx=15)
   
   if not games:
      # print("NO game shortcuts found")
      customtkinter.CTkLabel(my_frame, text="No games found. Add a non-steam game to steam first.", justify="center").grid(row=0, column=0, pady=15)
   else:
      switch_val.clear()
      counter = 0
      for g in games:
         switch_val.insert(counter,get_steam_input_status(g["appid"]))
         customtkinter.CTkLabel(my_frame, text=g["AppName"], wraplength=250,  justify="left").grid(row=counter, column=0,  sticky="w", padx=10, pady=5)
         customtkinter.CTkSwitch(my_frame, text="", variable=switch_val[counter], onvalue="1", offvalue="0", width=10, command=functools.partial(on_switch_value_changed, g, counter)).grid(row=counter, column=1, pady=5, padx=15)
         counter+=1

# get steam input value from config
def get_steam_input_status(appid):
   try:
      d = vdf.parse(open(USERDATA_PATH + id + LOCALCONFIG_VDF_PATH, encoding="utf8"))
      steam_settings = d["UserLocalConfigStore"]["apps"][str(appid)]
      if "UseSteamControllerConfig" in steam_settings:
         return customtkinter.StringVar(value=steam_settings["UseSteamControllerConfig"])
      else:
         return customtkinter.StringVar(value="1")
   except:
      return customtkinter.StringVar(value="1")

def on_combobox_click(choice):
   global chosen_filter
   chosen_filter = choice
   modified_games.clear()
   my_frame.destroy()
   display_scroll_frame(chosen_filter)

# set UseSteamControllerConfig to 1 to enable and 0 to disable the steam input
def on_switch_value_changed(game,index):
   value = str(switch_val[index].get())
   modified_games[game["appid"]] = {"UseSteamControllerConfig": value, "SteamControllerRumble": "-1", "SteamControllerRumbleIntensity": "320"  }

def on_exit_button():
   exit()

def on_save_button():
   msg = CTkMessagebox(title="Save?", message="Make sure Steam is NOT running.\nSave configuration?",icon="question", option_1="Save", option_2="Cancel", width=400, height=200, justify="center")
   response = msg.get()

   if response=="Save":
      if is_steam_running() == 0:
         # cannot save new config if steam is running since it will be overwritten with the backup 
         show_generic_info("Save error","Steam is currently running.\nClose Steam first.", "warning","Back")
      elif modified_games:
         ret = set_steam_input()
         if ret:
            on_combobox_click(chosen_filter)
            show_generic_info("Save error", "Cannot save this modification. Changes reverted.","cancel","Back")
         else:
            modified_games.clear()
            show_generic_info("Save successful", "Modifications saved successfully.","check","Back")
      else:
        show_generic_info("No changes","No modifications have been made.", "info","Back")
   else:
      if modified_games:
         on_combobox_click(chosen_filter)

def on_fatal_error(message,title):
   msg = CTkMessagebox(title=title, message=message,icon="warning", option_1="Exit", width=400, height=200)
   response = msg.get()

   if response or response is None:
      exit()

def show_generic_info(title, message, icon, button_text):
   CTkMessagebox(title=title, message=message,icon=icon, option_1=button_text, width=400, height=200)

# set steam input value in config
def set_steam_input():
   try:
      d = vdf.parse(open(USERDATA_PATH + str(id) + LOCALCONFIG_VDF_PATH, encoding="utf8"))
      if "apps" not in d["UserLocalConfigStore"]:
         d["UserLocalConfigStore"]["apps"] = {}
      for appid in modified_games:
         if str(appid) not in d["UserLocalConfigStore"]["apps"]:
            d["UserLocalConfigStore"]["apps"][str(appid)] = {}
         for element in modified_games[appid]:
            d["UserLocalConfigStore"]["apps"][str(appid)][element] = modified_games[appid][element]
      vdf.dump(d, open(USERDATA_PATH + id + LOCALCONFIG_VDF_PATH,'w', encoding="utf8"), pretty=True)
      return None
   except:
      print("something went wrong")
      return 1

# main
app = customtkinter.CTk()
app.wm_iconbitmap()
app.iconphoto(True, PhotoImage(data=ICON_DATA))
app.resizable(0,0)
app.title("Steam Input Disabler v"+APP_VERSION)

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

id = get_current_user()
shortcuts = read_shortcuts()

if id is None:
   on_fatal_error("Cannot find user","User error")

name = get_user_name()

if shortcuts is None:
   on_fatal_error("NO non-Steam game shortcuts found.", "Games not found")
   
chosen_filter = FILTER_LUTRIS
switch_val = []
modified_games = {}

customtkinter.CTkLabel(master=app, text="User: "+name, wraplength=250, justify="left").grid(row=0, column=0, sticky="w", padx=15, pady=15)
combobox = customtkinter.CTkComboBox(master=app,
   values=[FILTER_ALL, FILTER_LUTRIS, FILTER_HEROIC],
   command=on_combobox_click)
combobox.set(chosen_filter)
combobox.grid(row=0, column=1, sticky="e", padx=15, pady=15)

display_scroll_frame(chosen_filter)

button = customtkinter.CTkButton(master=app, text="Save", command=on_save_button)
button.grid(row=2, column=0, pady=20)

button2 = customtkinter.CTkButton(master=app, text="Exit", command=on_exit_button)
button2.grid(row=2, column=1, pady=20)

app.mainloop()