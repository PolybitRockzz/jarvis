from plyer import notification
from playsound import playsound
import json
import time
from datetime import datetime

from modules.logging import logging_error

def tell_time():
    time = datetime.now().strftime("%I:%M %p")
    return time

def tell_date():
    date = datetime.now().strftime("%A, %B %d, %Y")
    return date

def tell_day():
    day = datetime.now().strftime("%A")
    return day

def tell_date_and_time():
    date_and_time = datetime.now().strftime("%A, %B %d, %Y - %I:%M %p")
    return date_and_time

def reminders_thread():
    while True:
        time.sleep(1)
        try:
            with open('reminders.json', 'r') as reminders_file:
                data = json.load(reminders_file)
            
            updated_data = []
            current_time = time.time()

            for reminder in data:
                if abs(current_time - int(reminder['time'])) < 60:
                    notification.notify(
                        title=reminder['title'],
                        message=reminder['message'],
                        timeout=10
                    )
                    playsound('assets\\beep.mp3')  # Play sound effect
                else:
                    updated_data.append(reminder)
            
            with open('reminders.json', 'w') as reminders_file:
                json.dump(updated_data, reminders_file, indent=2)
        
        except FileNotFoundError:
            with open('reminders.json', 'w') as reminders_file:
                json.dump([], reminders_file)
        
        except Exception as e:
            logging_error(e)

def add_reminder(title, message, reminder_time: datetime):
    try:
        try:
            with open('reminders.json', 'r') as reminders_file:
                data = json.load(reminders_file)
        except FileNotFoundError:
            data = []

        data.append({
            'title': title,
            'message': message,
            'time': reminder_time.timestamp()
        })

        with open('reminders.json', 'w') as reminders_file:
            json.dump(data, reminders_file, indent=2)

    except Exception as e:
        logging_error(e)

def upcoming_reminders(threshold: int):
    try:
        with open('reminders.json', 'r') as reminders_file:
            data = json.load(reminders_file)

        upcoming_reminders = []

        for reminder in data:
            if abs(time.time() - int(reminder['time'])) < threshold:
                upcoming_reminders.append(reminder)

        return upcoming_reminders

    except Exception as e:
        logging_error(e)