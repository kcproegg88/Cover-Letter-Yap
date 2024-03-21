import os
from datetime import datetime


def init_setup(main_dir="user_name", number_of_paragraphs=3):

    working = init_main_dir(main_dir)
    sub_dirs = ["introduction", "conclusion"]
    [sub_dirs.append(f"paragraphs_{i}") for i in range(number_of_paragraphs)]

    paragraphs = 0
    while working:
        working = create_sub_dir(sub_dirs[paragraphs], main_dir)
        for i in range(3):
            create_file(f"{i+1}.txt", sub_dirs[paragraphs], main_dir) git
        paragraphs += 1
        if paragraphs > number_of_paragraphs + 1:
            print(f"Setup Successful, Introduction, Conclusion and {number_of_paragraphs} paragraphs created.\n")
            break

    return working


def init_main_dir(main_dir="user_name"):
    try:
        os.mkdir(main_dir)
        print(f"Folder '{main_dir}' created successfully at {datetime.now}.")
        return 1
    except FileExistsError:
        print(f"Folder '{main_dir}' exists already.\n")
        return 1
    except OSError as e:
        print(f"Error occurred while creating folder '{main_dir}': {e}\n")
        return 0

def create_sub_dir(sub_dir, main_dir="user_name"):
    nested_folder_path = os.path.join(main_dir, sub_dir)
    try:
        os.mkdir(nested_folder_path)
        print(f"\tFolder '{sub_dir}' created successfully under '{main_dir}'at {datetime.now}.")
        return 1
    except FileExistsError:
        print(f"\tFolder '{sub_dir}' exists under '{main_dir}'already.\n")
        return 1
    except OSError as e:
        print(f"Error occurred while creating folder '{sub_dir}' under '{main_dir}': {e}\n")
        return 0


def create_file(file_name , sub_dir, main_dir="user_name"):
    nested_folder_path = os.path.join(main_dir, sub_dir)
    file_path = os.path.join(main_dir, sub_dir)
    try:
        if os.path.exists(file_path):
            print(f"Text file '{file_name}' already exists inside '{nested_folder_path}'.")
            return 1
        with open(file_path, 'w') as file:
            file_written_name = file_name[:-2]
            sub_dir_written_name = sub_dir.split("_").join()
            file.write(f"This is sample {sub_dir_written_name}, {file_written_name}: My name is [name], I want to work"
                       f"at [company], as a [position]. You can contact me at [phone] or [email].")
            print(f"Text File '{file_name}' created successfully under '{nested_folder_path}' at {datetime.now}")
            return 1
    except OSError as e:
        print(f"Error occurred while creating file '{file_name}' under '{nested_folder_path}': {e}\n")
        return 0
