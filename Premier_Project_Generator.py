from multiprocessing import process
import os
import time
import shutil
import win32gui
import win32com.client
import win32clipboard
import win32process
import win32pdhutil
import wmi
import keyboard
from pynput import mouse
import sys
import win32pdhutil
import wmi


d

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)  
 
premier_empty_project = resource_path("EmptyProject.prproj")
#premier_empty_project = resource_path("project_files\EmptyProject.prproj")


def is_file_explorer():
    procs = wmi.WMI().Win32_Process()

    pycwnd = win32gui.GetForegroundWindow()
    tid, pid = win32process.GetWindowThreadProcessId(pycwnd)

    for proc in procs:
            if proc.ProcessId == pid:
                if (proc.ExecutablePath == "C:\\WINDOWS\\Explorer.EXE"):
                    return True
                else    :
                    print("not File Explorer but: " )
                    for proc in procs:
                        if proc.ProcessId == pid:
                            print('pid', pid)
                            print( 'exec', proc.ExecutablePath)
                            print ('title', win32gui.GetWindowText(pycwnd))
                    print("plase use only in file exlorer")
                    return False
                    
        


def create_editing_folders():

    global active_folder_path, project_name
    

    #empty Clipboard
    win32clipboard.OpenClipboard(0)
    win32clipboard.EmptyClipboard()
    win32clipboard.CloseClipboard()
  
    keyboard.press_and_release('ctrl+l')
    keyboard.press_and_release('ctrl+c')
    time.sleep(0.2)
    
    win32clipboard.OpenClipboard(0)
    active_folder_path = win32clipboard.GetClipboardData()
    print(active_folder_path)
    win32clipboard.CloseClipboard()

    #Create a new folders
   

    new_folder(active_folder_path, "Edit")
    new_folder(active_folder_path, "Sound")
    new_folder(active_folder_path, "Videos")
    
    #new_project_path = os.path.join(active_folder_path, "new.pproj")
    #premier_pro.Newproject(new_project_path)
    
    # Get the project name from the active folder path
    project_name = os.path.split(active_folder_path)[1]
   
    
    print("your project name is: ", project_name)
    #___________________________________________________________________________________________________
    
    
    
    #print("premier project creted", new_project_path)
     #____________________________________________________
  

   
def create_premier_project(empty_premier_project_file):
    print("creating project")  
    # Copy a file to the active folder path with the project name as the file name
    premier_destiny_path = os.path.join(active_folder_path,"Edit", project_name + ".prproj")
    shutil.copy(empty_premier_project_file, premier_destiny_path)
    print("premier project file copied to", premier_destiny_path)  

def new_folder(folder_path, folder_name):
    new_folder_path = os.path.join(folder_path, folder_name)
    os.makedirs(new_folder_path, exist_ok=True)
    print("Folder ",folder_name, "created at:", new_folder_path)


# Wait for the user to press the spacebar key
print(" ")
from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    if pressed and button == button.left:
        global click_count
        click_count += 1
        if click_count == 2:
            time.sleep(0.1)
            keyboard.press_and_release('enter')
            time.sleep(0.2)

            create_editing_folders()
            create_premier_project(premier_empty_project)
            print("all done!")
            listener.stop()
            exit(1)

            
    
   


            click_count = 0
print("starting")
#if is_file_explorer() == True:
#    print("its File Explorer")
click_count = 0
with Listener(on_click=on_click) as listener:
        listener.join()

