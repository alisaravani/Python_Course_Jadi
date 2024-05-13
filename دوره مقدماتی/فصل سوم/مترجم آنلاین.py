from collections import OrderedDict
strN=int(input())
List1=[]
myDict=OrderedDict()

for i in range(strN):
    strInput=input()
    strfind=strInput.find(" ")
    myDict[strInput[:strfind]]={strInput[strfind:].strip()}

strSentence=input().split()
strFinal=[]
strNewFinal=""

for thisOne in strSentence:
    if thisOne in myDict:
        strFinal+=myDict.get(thisOne)
    else:
        strFinal.append(thisOne)


for i in range(len(strFinal)):
    strNewFinal+=strFinal[i]+" "
print (strNewFinal)
