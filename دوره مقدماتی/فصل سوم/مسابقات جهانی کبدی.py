strNafar=input()
strSabeghe=input()
Sabeghe=0
Count=0
strSabeghe=strSabeghe.split()
for i in range(len(strSabeghe)):
   Sabeghe =strSabeghe.pop()
   if int(Sabeghe)<=2:
        Count=Count+1 
    

print(int(Count/3))
