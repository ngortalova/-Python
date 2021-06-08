import os
import json

folder = os.getcwd()
print(folder)
folder_name = os.path.basename(folder)
print(folder_name)
folder_size_stat = {}
list_size = []
roots = []
for root, dirs, files in os.walk(folder):
    list_size_temp = [item.stat().st_size for item in os.scandir(root)]
    list_size.extend(list_size_temp)
    roots.append(root)
k = max(list_size)
size_threshold = 1
size_threshold2 = 10 * 10**2


def dict_creation(size_1, size_2):
    tmp = set()
    list_of_files = []
    for root in roots:
        list_of_files_temp = [item.name for item in os.scandir(root) if size_1 <= item.stat().st_size < size_2]
        list_of_files.extend(list_of_files_temp)
    for i in range(len(list_of_files)):
        if "." in list_of_files[i]:
            ext_list = list_of_files[i].split(".")
            tmp.add(ext_list[-1])
    file_ext_list = list(tmp)
    folder_size_stat[size_threshold2] = (len(list_of_files), file_ext_list)


while k > size_threshold2:
    dict_creation(size_threshold, size_threshold2)
    size_threshold = size_threshold2
    size_threshold2 *= 10

dict_creation(size_threshold, size_threshold2)
print(folder_size_stat)

with open(f'{folder_name}_summary.json', "w", encoding="utf-8") as f:
    json.dump(folder_size_stat, f)
