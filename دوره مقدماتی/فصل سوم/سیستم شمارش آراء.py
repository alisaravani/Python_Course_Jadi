from collections import OrderedDict
strN=int(input())
List1=[]

myDict=OrderedDict()

for i in range(strN):
    List1.append(input())
    
    
for i in List1:
    myDict[i]=myDict.get(i,0)+1

List2=list(myDict.keys())
List2.sort()

for thisOne in List2:
    print("%s %s"%(thisOne,myDict[thisOne]))
