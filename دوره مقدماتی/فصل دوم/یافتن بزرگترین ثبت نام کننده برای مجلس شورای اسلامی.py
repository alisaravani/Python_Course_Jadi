age=int(input())
age_max=0
while age != -1:
    if age>age_max:
        age_max=age
    age=int(input())
print(age_max)
