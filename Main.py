import sys
import re

if __name__ == "__main__":
    """inputFile = sys.argv[1]
    outputFile = sys.argv[2]"""
    count = 0
    file = open("text.txt", "r")
    soru = ""
    option =""
    sorulist = []
    for text in file:
        question = re.search("\A[0-9][.]$|\A[0-9][)]$|\ASoru [0-9]$", text)
        if question == None:
            soru += text
        else:
            sorulist.append(soru)
    for x in sorulist:
        print(x)
        print("-----------------------")

