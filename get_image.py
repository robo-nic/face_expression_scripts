import urllib.request
import time

##################

filename = 'sad human face images.txt'
toSaveAtDirName = 'sad_raw'

# this can be changed, in case some photos are already downloaded,
# the index will be printed in the console

# crashed at index: 1105
# resuming now from: 1106

# crashed at index: 1982
# resuming now from: 1983

# crashed at index: 2279
# resuming now from: 2280

# stopped at index: 3124
# resuming now from: 3124

# 3263

# 5421
startFromIndex = 5421

# 5801
startFromIndex = 5802

# 5809
startFromIndex = 5809

# 6840
startFromIndex = 6841

# 8945
startFromIndex = 8946
##################

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
