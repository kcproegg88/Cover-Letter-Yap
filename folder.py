import os
from datetime import datetime


def create_maindir(name="user_name"):  # Creates the Main Folder
    try:
        os.mkdir(name)
        print(f"Folder '{name}' created successfully at {datetime.now}.")
        return 1
    except FileExistsError:
        print(f"Folder '{name}' exists already.\n")
        return 1
    except OSError as e:
        print(f"Error occurred while creating folder '{name}'.\n")
        return 0


def create_subdir(sub_folder, name="user_name"):
    nested_folder_path = os.path.join(name, sub_folder)
    try:
        os.mkdir(nested_folder_path)
        print(f"\tFolder '{sub_folder}' created successfully under {name} at {datetime.now}.")
        return 1
    except FileExistsError:
        print(f"\tFolder '{sub_folder}' already exists under {name}.")
        return 1
    except OSError:
        print(f"\tError occurred while creating folder '{sub_folder}' under {name}.\n")
        return 0

def create_file(file_name, sub_folder,name="user_name"):
    nested_folder_path = os.path.join(name, sub_folder)
    text_file_path = os.path.join(nested_folder_path, file_name)
    try:
        if os.path.exists(text_file_path):
            print(f"Text file '{file_name}' already exists inside '{sub_folder}'.")
            return 1
        with open(text_file_path, 'w') as file:
            print(f"Text file '{file_name}' created successfully inside '{sub_folder}' at {datetime.now}.")
            return 1
    except OSError as e:
        print(f"Error occurred while creating text file '{file_name}' inside '{sub_folder}'.")
        return 0


def init_file(file_name, sub_folder, name="user_name"):
    pass


def init_folders(name="user_name"):
    running = create_maindir()