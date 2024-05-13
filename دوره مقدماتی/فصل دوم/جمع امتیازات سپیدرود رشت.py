
count_Win=0
Points=0
for i in range(0,30):
    p1=int(input())
    if p1==3:
        count_Win=count_Win+1
        Points=p1+Points
    else:
        Points=p1+Points
print(Points,count_Win)
