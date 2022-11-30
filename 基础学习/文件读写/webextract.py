def main():
    inputfile = 'graphic.html'
    outputfile = 'graphics.txt'
    htmlLines = getHTMLlines(inputfile)
    imageUrls = extractImageUrls(htmlLines)
    showResults(imageUrls)
    saveResults(outputfile, imageUrls)


def getHTMLlines(inputfile):
    f = open(inputfile, 'r', encoding='utf-8')
    ls = f.readlines()
    f.close()
    return ls


def extractImageUrls(htmlLines):
    urls = []
    for line in htmlLines:
        if 'img' in line:
            url = line.split('src="')[-1].split('"')[0]
            if url.endswith(('jpg', 'JPG', 'JPEG', 'jpeg', 'png')):
                urls.append(url)
    return urls


def showResults(imageUrls):
    count = 0
    for url in imageUrls:
        print(f'第{count:2}个URL：{url}')
        count += 1


def saveResults(outputfile, imageUrls):
    f = open(outputfile, 'w')
    for url in imageUrls:
        f.write(url + '\n')
    f.close()


main()
