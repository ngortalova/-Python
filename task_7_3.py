import os
import shutil

WORK_DIR = os.path.abspath("--my_project")

list_of_temps = []
for root, dirs, files in os.walk(WORK_DIR):
    if root.endswith("--templates"):
        list_of_temps.append(root)
print(list_of_temps)

new_temp_folder = os.path.join(WORK_DIR, "--templates")
os.mkdir(new_temp_folder)


def copytree(src, dst):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)


for el in range(len(list_of_temps)):
    copytree(list_of_temps[el], new_temp_folder)
