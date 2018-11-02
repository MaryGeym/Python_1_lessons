# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.



import os
import shutil
import sys
dirdir =[('dir_' + str(i + 1)) for  i in range(9)]

def make_dir(dirs):
    dir_path = os.path.join(os.getcwd(),dirs)

    try:
        os.mkdir(dir_path)
    except:
        print('Такая директория уже существует')



# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def list_dir(main_path):
    for _ in os.listdir(main_path):
        print(_)
main_path = os.getcwd()



# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil
import sys
def make_copy(file_1,new_file):
    shutil.copy(file_1,new_file)

