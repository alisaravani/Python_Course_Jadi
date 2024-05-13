strfinal=""
strinput=input()
strArray=[]
for i in strinput:
  if i.isdigit():
    strArray.append(i)

strArray.sort()
for i in strArray:
  strfinal=strfinal + i + "+"


print(strfinal[:-1])
