strPut=[]
strFirstChar=[]
i=0
while i<10:
    strSimple=input()
    strSimple=strSimple.lower()
    strfinal=strSimple.replace(strSimple[0],strSimple[0].upper(),1)
    strPut.append(strfinal)
    i=i+1

for i in strPut:
    print(i)
