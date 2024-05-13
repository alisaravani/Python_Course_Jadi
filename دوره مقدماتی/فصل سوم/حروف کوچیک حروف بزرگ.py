strInput=input()
U1=0
L1=0
for i in range (len(strInput)):
    s=strInput[i]
    if s.isupper():
        U1=U1+1
    else:
        L1=L1+1
if U1>L1:
    print(strInput.upper())
else:
    print(strInput.lower())
