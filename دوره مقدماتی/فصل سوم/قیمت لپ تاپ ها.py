strInput=""
ListPrice,ListQuality=[],[]
intIndex=0

n=int(input())
for i in range(0,n):
    strInput=input()
    ListPrice.append(int(strInput[0:strInput.index(" ")]))
    ListQuality.append(int(strInput[strInput.index(" ")+1:]))
for i in range(0,n):
    for j in range(0,n):
        if ListPrice[i]<=ListPrice[j] and ListQuality[i]>=ListQuality[j] and i!=j:
            intIndex+=1

if intIndex>=1:
    print("happy irsa")
else:
    print("poor irsa")
