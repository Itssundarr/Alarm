import os
import webbrowser
import datetime

os.system("cls")

print("\n------------------SET YOUR ALARM-----------------------\n")
Date = input("Enter the date in DD-MM-YYYY: ")
Hour = int(input("Set the Hour : "))
Minute = int(input("Set the minutes : "))
Am_Pm = input("AM or PM : ")
Reason = input("Enter the Reason for the Remainder : ")

os.system("cls")

if Am_Pm == "PM" or Am_Pm == "pm":
    Hour += 12

if Minute<10 and Hour<10:
    print(f"Your alarm is set at 0{Hour}:0{Minute} {Am_Pm}.\nReason : {Reason}.\n\nYou can DEEP WORK on your tasks at ease without the anxiety of remembering the remainder.")
else:
    print(f"Your alarm is set at {Hour}:{Minute} {Am_Pm}.\nReason : {Reason}.\n\nYou can DEEP WORK on your tasks at ease without the anxiety of remembering the remainder.")

os.system("cls")

while True:
    if Date == datetime.datetime.now().strftime('%d-%m-%Y') and Hour == datetime.datetime.now().hour and Minute == datetime.datetime.now().minute:
        if Hour<10 and Minute<10:
           print(f"It's {Date} - 0{Hour}:0{Minute} {Am_Pm}.\nYou told us to remaind for {Reason}.\n\n")
        else:
            print(f"It's {Date} - {Hour}:{Minute} {Am_Pm}.\nYou told us to remaind for {Reason}.\n\n")

        webbrowser.open_new("https://www.youtube.com/watch?v=kPhpHvnnn0Q")

        break