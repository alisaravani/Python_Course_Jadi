ListEntry,TotalList=[],[]
mydict=dict()
NPerson=int(input())
for i in range(0,NPerson):
    ListEntry.append(input())


for word in ListEntry:
    word=word.split()
    for j in range(1,4):
        TotalList.append(word[j])

mydict.update({"Action":TotalList.count("Action")})
mydict.update({"Adventure":TotalList.count("Adventure")})
mydict.update({"Comedy":TotalList.count("Comedy")})
mydict.update({"History":TotalList.count("History")})
mydict.update({"Horror":TotalList.count("Horror")})
mydict.update({"Romance":TotalList.count("Romance")})


mydict=dict(sorted(mydict.items(), key=lambda x:x[1],reverse=True))

for x in mydict:
    print("%s : %s"%(x,mydict.get(x)))
