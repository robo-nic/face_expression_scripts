"""

THIS SCRIPT WORKS ONLY ON THE 123RF.COM WEBSITE

"""

import requests
from bs4 import BeautifulSoup

# USER INPUT DATA
searchFor = 'surprised human face'
totalImages = 10000

###################################
# change the following variable only when you have interrupted the scirpt
# and you have the page number in the console

pageNumber = 0

###################################
###################################
###################################

# headers use korchi just to that their server dont think we are a bot
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def getNextPageUrl(num):
    print('Downloading for page number:', num)

    url = 'https://www.123rf.com/stock-photo/' + searchFor.replace(' ', '_') + '.html?oriSearch=' + \
        searchFor + '&safe_search=off&start=' + \
        str(num) + '10&sti=lv2oceequ4qnw820q1'

    print('URL:', url)

    return url


numberOfImages = 0

while numberOfImages < totalImages:

    imageURLs = []

    pageNumber += 1

    response = requests.get(getNextPageUrl(pageNumber), headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    imageSourceClassName = 'imgSrcClass'
    for imageTag in soup.findAll('img', {'class': imageSourceClassName}):
        imageURLs.append(imageTag.get('src'))

    numberOfImages += len(imageURLs)

    # write all the files before running the next loop
    # finally writing the image URLs to file

    with open(searchFor + ' images.txt', 'a') as f:
        f.write('\nImages from page number: ' + str(pageNumber) + '\n\n')
        for imageUrl in imageURLs:
            f.write(imageUrl)
            f.write('\n')
