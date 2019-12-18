import os
import os.path
import shutil


def createAndMove(dirName, file):
    try:
        os.makedirs(dirName)
        shutil.move(f'./{file}', f'./{dirName}/{file}')
        print("Directory ", dirName, " Created ")
    except FileExistsError:
        shutil.move(f'./{file}', f'./{dirName}/{file}')


files = os.listdir('./')

exts = set()

for file in files:
    fileExt = os.path.splitext(file)[-1].lower()
    exts.add(fileExt[1:])

exts.remove('')


def compareandcreate(file):
    fileE = os.path.splitext(file)[-1][1:].lower()
    isFile = os.path.isfile(file)
    if fileE in exts:
        if isFile and file != 'sort.py':
            fileName = f'{fileE}Folder'
            createAndMove(fileName, file)
    else:
        if isFile:
            createAndMove('anotherExt', file)


x = map(compareandcreate, files)
print(list(x))

print('Your Files Had Been Sorted')