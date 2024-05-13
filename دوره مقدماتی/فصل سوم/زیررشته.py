NewStrInput=""
strfinal=0

strInput=input().lower()
strfinal= strInput.find("ab")

if strfinal>=0:
    NewStrInput=strInput.replace("ab","",1)
    strfinal=0  

strfinal=NewStrInput.find("ba")
if strfinal>=0:
    print("YES")
else:
    print("NO")
