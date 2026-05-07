import pandas as pd 
import datetime
from Speak import speak
def birthday_dates():
    df = pd.read_excel('dates.xlsx') 
    # Get today's date 
    today = datetime.datetime.today()

    # Get birthdays from the Excel file 
    birthdays = df[['Name', 'DOB']]

    # Iterate over the birthdays 
    printed = False
    for index, row in birthdays.iterrows(): 
        if today.strftime("%d-%m") == row['DOB'].strftime("%d-%m"): 
            speak("Today is {}'s birthday!".format(row['Name'])) 
            printed = True
            
    if not printed:
        print("Today is no one's birthday!")
