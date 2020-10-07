import urllib.request
import time

##################

filename = 'surprised human face images.txt'
toSaveAtDirName = 'surprised_raw'

startFromIndex = 0

imagesList = set()

with open(filename) as file:
    tmp = file.readlines()

    print(len(tmp))

    for value in tmp:
        if(value.startswith('http')):
            imagesList.add(value)

imagesList = list(imagesList)

print('Total images to download:', len(imagesList))


def getFileName(dirName):
    # assuming all the images are of type jpg
    return dirName + '/' + str(time.time_ns()) + '.jpg'


for i in range(startFromIndex, len(imagesList)):
    print('Downloading file of index:', i)
    try:
        urllib.request.urlretrieve(imagesList[i], getFileName(toSaveAtDirName))
    except:
        print('Failed for index:', i)
