import os

def changeFilePath(filePath):
    os.chdir(filePath)

def createTextFile(outFile) :
    valueList = range(10)
    for i in valueList :
        outFile.write(str(i) + '\n')
    outFile.close()

def readFile(fileName) :
    fileData = []
    fileObject = open(fileName, 'r')
    while True:
        lineValue = fileObject.readline()
        if lineValue == '':
            break
        fileData.append(int(lineValue.strip()))

    return fileData

if __name__ == "__main__":
    filePath = r"C:\ust_work"
    fileName = "first.txt"
    outFile = open(fileName, "w")

    changeFilePath(filePath)
    createTextFile(outFile)
    print(readFile(fileName))