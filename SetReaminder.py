from Speak import speak
from datetime import datetime
from datetime import timedelta
from plyer import notification
import time

#Taking input 
today = datetime.now()
today_date = (today.strftime('%d-%m'))

date_in = input("After how many days do you want to set remainder: ")
def remainder_noti():
    days = int(date_in) if date_in.isdigit() else 0
    if date_in.lower() == "today":
        days = 0

    remainder = input("Enter your remainder: ")
    time_input = input("Enter a time in hh:mm format: ")
    date_input = today_date
    date_time = datetime.strptime(date_input + ' ' + time_input, '%d-%m %H:%M')
    date_time = date_time + timedelta(days=days, hours=0, minutes=0)

    speak("Reminder set for {}".format(date_time.strftime('%d-%m %H:%M')))

    #Print reminder
    while True:
        if time.strftime("%d-%m %H:%M") == date_time.strftime('%d-%m %H:%M'):
            speak("The reminder is: " + remainder)

            notification.notify(
                title='Notification Remainder from Gyani',
                message=remainder,
                app_icon="Gyani.ico",
                timeout=10,
            )
            break
        time.sleep(1)
