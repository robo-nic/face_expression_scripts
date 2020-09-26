imagesList = set()

with open('sad face images.txt') as file:
    tmp = file.readlines()

    print(len(tmp))

    for value in tmp:
        if(value.startswith('http')):
            imagesList.add(value)


print(len(imagesList))

with open('thetry file.txt', 'w') as f:
    for imageUrl in imagesList:
        f.write(imageUrl)
        f.write('\n')
