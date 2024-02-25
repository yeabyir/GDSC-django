import os
import shutil
import time

def list_files():
    return os.listdir()

def is_recently_modified(file):
    stats = os.stat(file)
    current_time = time.time()
    modification_time = stats.st_mtime
    if current_time - modification_time < 86400:
        return True
    else:
        return False


def update_files(files):
    for file in files:
        try:
            with open(file, 'w') as f:
                f.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '\n')
        except IOError as e:
            print(f"Error updating {file}: {e}")

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def move_files(files, folder_name):
    create_folder(folder_name)  # Ensure the destination folder exists
    for file in files:
        destination = os.path.join(folder_name, os.path.basename(file))
        if not os.path.exists(destination):
            shutil.move(file, destination)
        else:
            print(f"File {file} already exists in {folder_name}. Skipping.")



files = list_files()

recent_files = [file for file in files if is_recently_modified(file)]
update_files(recent_files)
create_folder('last_24hours')
move_files(recent_files, 'last_24hours')
