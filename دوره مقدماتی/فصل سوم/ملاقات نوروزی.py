strInput=input()
strInput=strInput.split()
List1=[]

for i in range(len(strInput)):
    List1.append(int(strInput[i]))

print(max(List1)-min(List1))
