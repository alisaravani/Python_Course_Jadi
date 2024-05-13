strN=int(input())
List1=[]
ListPrice=[]
ListQuality=[]
strFind=0
strTest=""
Count=0

for i in range(strN):
    List1.append(input())
    strTest=str(List1[i])
    strFind=strTest.find(" ")
    ListPrice.append(int(strTest[:strFind]))
    ListQuality.append(int(strTest[strFind:]))

min1=ListPrice.index(min(ListPrice))
pop1=min(ListPrice)
p1=ListQuality[min1]
ListPrice.pop(min1)
ListQuality.pop(min1)

for i in range(strN):
    if len(ListPrice)>0 or len(ListQuality)>0:
        pop2=ListPrice.pop()
        p2=ListQuality.pop()

        if(pop1<pop2) and p1>p2:
            Count=1
            break
        else:
            Count=0
if Count>0:
    print("happy irsa")
else:
    print("poor irsa")
