import math

strlist=0
strtext=""
strfind=0
strsqrList=[]
strN=int(input())

for i in range (strN):
    strlist=int(input())
    strsqrList.append(math.sqrt(strlist))


for i in strsqrList:
    strtext=str(i)
    if len(strtext)>8:
        strfind=strtext.find(".")+5
        print(strtext[:strfind])
    else:
        strFinal="{:.4f}"
        print(strFinal.format(i))
