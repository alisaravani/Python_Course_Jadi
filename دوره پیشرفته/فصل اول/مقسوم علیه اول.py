def maghsom(InputNumber):
    ListMaghsom=[]

    for i in range(1,InputNumber+1):
        if InputNumber%i==0:
            ListMaghsom.append(i)
    
    return ListMaghsom


def aval(inputNumber):
    count=0
    for i in range(1,inputNumber):
        if inputNumber%i==0:
            count+=1
    if count==1:
        return 1
    else:
        return 0


intInput=0
ListNumber=[]
ListMaghsom=[]
ListAval=[]
ListResult=[]
ListSec=[]

for i in range(0,10):
    intInput=int(input())
    ListNumber.append(intInput)
    ListMaghsom=maghsom(intInput)

    for j in ListMaghsom:
        if aval(j)==1:
            ListAval.append(j)

    ListResult.append(len(ListAval))
    ListMaghsom.clear()
    ListAval.clear()

if ListResult.count(max(ListResult))==1:
    indexNumber=ListResult.index(max(ListResult))
    print("%i %i"%(ListNumber[indexNumber],ListResult[indexNumber]))

else:
    maxNumber=max(ListResult)
    for k in range(len(ListNumber)):
        if ListResult[k]==maxNumber:
            ListSec.append(ListNumber[k])
    ListSec.sort(reverse=True)
    print("%i %i"%(ListSec[0],maxNumber))
