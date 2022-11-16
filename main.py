from pathlib import Path
import os
import re

WSL_base_path = r"/mnt/"
disk_on_WSL = "d/"
directory = r"University/Комп'ютерні технології статистичної обробки даних"
our_files = Path(WSL_base_path + disk_on_WSL + directory)

full_name = "Антон Омеляненко"
type_files_to_create = ['xlsx', 'docx']

for index, item in enumerate(range(8)):
    file_directory = f'/Лаб. {index + 1}'
    create_directory = our_files.__fspath__() + file_directory

    if os.path.isdir(create_directory) is False:
        os.mkdir(create_directory)
    for file_extension in type_files_to_create:
        subject_name = re.sub('^(.*?)University/', '', our_files.__fspath__())
        file_to_create = create_directory + f'/Лаб. {index + 1} {full_name} {subject_name} .{file_extension}'
        if not os.path.isfile(file_to_create):
            f = open(file_to_create, "a")
            f.close()
            print(file_to_create)