strfinal=""
strSeda=["a","e","i","o","u"]
strinput=input().lower()
strArray=[]
for i in strinput:
  if i not in strSeda:
    strArray.append(i)

for i in strArray:
  strfinal=strfinal + "." + i 


print(strfinal)
