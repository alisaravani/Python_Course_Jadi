strHello="hello"
Count=0
strinput=input()
for i in strinput:
  if Count!=5 and i==strHello[Count]:
    Count=Count+1
if Count==5:
    print("YES")
else:
    print("NO")
