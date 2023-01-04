import sys
import os
import time     

# Translate the arguments into variables
bat_file = sys.argv[1]
folder_path = sys.argv[2]
folder_name = sys.argv[3]
edit_folder_switch = sys.argv[4]
sound_folder_switch = sys.argv[5]
videos_folder_switch = sys.argv[6]

# Print the variables
print(bat_file)
print(folder_path)
print(folder_name)

# Create the full path of the new folder
edit_folder_path = os.path.join(folder_path, "Edit")
sound_folder_path = os.path.join(folder_path, "Sound")
videos_folder_path = os.path.join(folder_path, "Videos")
  

# Create the new folder
if edit_folder_switch == "true":
    os.makedirs(edit_folder_path)
if sound_folder_switch == "true":
 os.makedirs(sound_folder_path)
if videos_folder_switch == "true":
    os.makedirs(videos_folder_path)


