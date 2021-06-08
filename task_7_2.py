import os


def create_root_folder(root_name):
    if not os.path.exists(root_name):
        os.mkdir(root_name)
    else:
        print(f"Папка {root_name} уже есть.")
        exit()


def create_file(name):
    if not os.path.exists(name):
        open(name, "x").close()


with open("config.yaml", "r", encoding="utf-8") as f:
    line = f.readline()
    root_orig = line[line.index("-"):].strip("\n")
    create_root_folder(root_orig)
    root_path = root_orig
    while line:
        line = f.readline()
        if line.startswith(" "):
            file_name = line[line.index("-"):].strip("\n")
            if line.count(' ') == 3:
                root_path = os.path.join(root_orig, file_name)
                os.mkdir(root_path)
                n = line.count(' ')
            elif file_name.lower().endswith('.py') or file_name.lower().endswith('.html'):
                create_file(os.path.join(root_path, file_name))
            else:
                if line.count(' ') <= n:
                    root_path = os.path.join(os.path.split(root_path)[0], file_name)
                    os.mkdir(root_path)
                    n = line.count(' ')
                else:
                    root_path = os.path.join(root_path, file_name)
                    os.mkdir(root_path)
                    n = line.count(' ')
print("Файлы созданы")
for root, dirs, files in os.walk(os.curdir):
    print(f"Root: \n\t{root} \nDirs: \n\t{dirs} \nFiles: \n\t{files}")
