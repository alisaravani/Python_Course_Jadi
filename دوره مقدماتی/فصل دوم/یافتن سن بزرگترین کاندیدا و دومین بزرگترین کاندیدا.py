age=[]
new_age=0
new_age=(int(input()))
while new_age != -1:
   age.append(new_age)
   new_age=(int(input()))
age.sort(reverse=True)


print(age[0], age[1])
