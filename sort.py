import os
import sys
import os.path as path
import shutil

if len(sys.argv) > 1:
    if (path.isdir(sys.argv[1])):
        dir = sys.argv[1]
        dir += '/' if dir[-1] != '/' else ''
    else:
        print("Please Enter Valid Directory ")
        exit()
else:
    dir = './'


def move(file, directory):
    source = dir + file
    dist = dir + directory + "/" + file
    shutil.move(source, dist)


def getExt(file):
    return path.splitext(file)[-1][1:].lower()


def sortFiles(files, folder, ext):
    for file in files:
        if file != f'sort.py':
            if (getExt(file) == ext):
                move(file, folder)
                print(f"{file}  moved successfully")


files = os.listdir(dir)
exts = set(getExt(file) for file in files if getExt(file))
for ext in exts:
    directory = f'{ext}Directory'
    parentDir = dir
    dir_path = path.join(parentDir, directory)
    if path.isdir(dir_path):
        sortFiles(files, directory, ext)
    else:
        os.mkdir(dir_path)
        print(f"{directory} Created successfully")
        sortFiles(files, directory, ext)
