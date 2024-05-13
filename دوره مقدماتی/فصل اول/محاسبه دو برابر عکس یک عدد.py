Number = int(input())
Reverse1=0
Reverse2=0
Reverse3=0

Reminder = Number %10
Reverse1 = (Reverse1 *10) + Reminder
Number = Number //10
Reminder = Number %10
Reverse2 = (Reverse2 *10) + Reminder
Number = Number //10
Reminder = Number %10
Reverse3 = (Reverse3 *10) + Reminder
Number = Number //10
mulReverse=str(Reverse1)+str(Reverse2)+str(Reverse3)
mulReverse=int(mulReverse)*2
print(mulReverse)
