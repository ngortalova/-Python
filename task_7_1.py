import os


def create_root_folder(root_name):
    if not os.path.exists(root_name):
        os.mkdir(root_name)
    else:
        folder_list[0] = input(f"Папка {root_name} уже есть. введите новое имя: ")
        create_root_folder(folder_list[0])


def create_folders(root_name, name):
    try:
        path_dir = os.path.join(root_name, name)
        os.mkdir(path_dir)
    except FileExistsError:
        print(f"Папка {name} уже есть")


folder_list = ["--my_project", "--settings", "--mainapp", "--adminapp", "--authapp"]
create_root_folder(folder_list[0])

for _ in range(1, len(folder_list)):
    create_folders(folder_list[0], folder_list[_])
    if _ != 1:
        create_folders(os.path.join(folder_list[0], folder_list[_]), "--templates")
