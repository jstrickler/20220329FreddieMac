import os

prefix = 'c'  # file to find
start_folder = '.'  # current folder

folder_to_skip = '.git'

for directory, subdirectories, file_names in os.walk(start_folder):
    if folder_to_skip in subdirectories:
        subdirectories.remove(folder_to_skip)
    for file_name in file_names:
        if file_name.startswith(prefix):
            target_path = os.path.join(directory, file_name)
            file_size = os.path.getsize(target_path)
            print(f"{file_size:8d} {target_path}")
