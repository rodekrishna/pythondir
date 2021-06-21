import sys
from sys import argv
def clock_angle(input_time):
    try:
        data = input_time.split(':')
        hour = int(data[0])
        minute = int(data[1])
        if(hour < 0 or minute <0 or hour > 12 or minute >60):
            raise Exception("Wrong Input!!")
        angle_hour=(360/12)*(hour+(minute/60))
        angle_minute=(360/60)*minute
        angle=float(abs(angle_hour-angle_minute))
        print("The time is {}:{} \n".format(hour,minute))
        print("Angle is {} degree \n".format(angle))
    except Exception:
        print("Please Enter valid Hour & Minute")
input=input()

print(data)
clock_angle(input_time)
