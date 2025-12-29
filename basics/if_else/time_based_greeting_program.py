#time based greeting program using if else
name=input("enter the name: ").capitalize()

import time
present_time=time.strftime("%H:%M:%S")

hour=int(time.strftime("%H"))

if(hour>=5 and hour<12):
    print("Good morning",name,"its time",present_time)

elif(hour>=12 and hour<17):
    print("Good afternoon",name,"its time",present_time)

elif(hour>=17 and hour<19):
    print("Good evening",name,"its time",present_time)

else:
    print("Good night",name,"its time",present_time)
