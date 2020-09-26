"""

THIS SCRIPT WORKS ONLY ON THE 123RF.COM WEBSITE

"""

import requests
from bs4 import BeautifulSoup

# USER INPUT DATA
searchFor = 'sad face'
totalImages = 20000

###################################
# change the following variable only when you have interrupted the scirpt
# and you have the page number in the console

pageNumber = -1

###################################
###################################
###################################

# headers use korchi just to that their server dont think we are a bot
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def getNextPageUrl(pageNumber):
    print('Downloading for page number:', pageNumber)

    url = 'https://www.123rf.com/stock-photo/' + searchFor.replace(' ', '_') + '.html?oriSearch=' + \
        searchFor + '&safe_search=off&start=' + \
        str(pageNumber) + '00&sti=lv2oceequ4qnw820q1'

    return url


numberOfImages = 0

imageURLs = set()

while numberOfImages < totalImages:

    pageNumber += 1

    response = requests.get(getNextPageUrl(pageNumber), headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    imageSourceClassName = 'imgSrcClass'
    for imageTag in soup.findAll('img', {'class': imageSourceClassName}):
        imageURLs.add(imageTag.get('src'))

    numberOfImages += len(imageURLs)

    # write all the files before running the next loop
    # finally writing the image URLs to file

    with open(searchFor + ' images.txt', 'a') as f:
        f.write('\nImages from page number: ' + str(pageNumber) + '\n\n')
        for imageUrl in imageURLs:
            f.write(imageUrl)
            f.write('\n')
