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

for file in files:
    fileExt = os.path.splitext(file)[1].lower()

    if fileExt == '.png' or fileExt == '.png~' or fileExt == '.jpg' or fileExt == '.jpeg' or fileExt == '.svg' or fileExt == '.gif':
        createAndMove('imgFolder', file)
    elif fileExt == '.pdf':
        createAndMove('pdfFolder', file)
    elif fileExt == '.zip' or fileExt == '.rar' or fileExt == '.gz' or fileExt == '.xz':
        createAndMove('zipFiles', file)
    elif fileExt == '.mp3':
        createAndMove('musicFolder', file)
    elif fileExt == '.sql':
        createAndMove('sqlFolder', file)
    elif fileExt == '.deb':
        createAndMove('debFolder', file)
    elif fileExt == '.mp4':
        createAndMove('videoFolder', file)
    elif fileExt == '.ttf':
        createAndMove('fontsFolder', file)
    elif fileExt == '.html' or fileExt == '.php' or fileExt == '.exe':
        createAndMove('codeFolder', file)
    else:
        isFile = os.path.isfile(file)
        if file != 'sort.py' and isFile:
            createAndMove('anotherExt', file)

print('your files had been formatted :D')
