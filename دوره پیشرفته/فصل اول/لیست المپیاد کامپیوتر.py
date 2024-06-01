ListEntry,TotalList,FinalList=[],[],[]
mydict=dict()
NPerson=int(input())
for i in range(0,NPerson):
    ListEntry.append(input())


for word in ListEntry:
    word=word.split(".")
    TotalList.append(word[0]+" "+ str.title(word[1])+" "+word[2])

TotalList.sort()
for person in TotalList:
    print(person)
