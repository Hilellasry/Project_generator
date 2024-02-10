@echo off

::what folders to add(Set to false to disable)
set "edit_folder=true"
set "sound_folder=true"
set "videos_folder=true"




:: Store the file paths in variables
set bat_file=%~dp0%~nx0
set folder_path=%1
set folder_name=%~nx1



:: Get the full path to the Python file
set python_file=%~dp0generator.py

:: Run the Python file with the file paths as arguments
python "%python_file%" "%bat_file%" "%folder_path%" "%folder_name%" "%edit_folder%" "%sound_folder%" "%videos_folder%"
::generator.exe "%bat_file%" "%folder_path%" "%folder_name%"


