from twilio.rest import Client
from datetime import datetime, timedelta
import time


acc_id='ACd4eb24b1926c1b3abcc533b14c63cb00'
aut_id='246900950b4b7ea4e2e8802a265ee2d2'

client=Client(acc_id,aut_id)

def send_whatsapp_message(recipient_number, message):
    try :
        recipient_number=f"whatsapp:+91{recipient_number}"
        message = client.messages.create(
            body=message,
            from_='whatsapp:+14155238886',
            to=recipient_number
        )
        print(message.sid)
    except Exception as e:
        print(e)

name =input("Enter recepient full name:")
number = input("Enter recepient number:")
message = input("Enter message:")
time_input = input("Enter time in HH:MM format:")
date = input("Enter date in DD/MM/YYYY format:")

scheedule_datetime = datetime.strptime(f"{date} {time_input}", "%d/%m/%Y %H:%M")
curr_datetime = datetime.now()

time_diff = scheedule_datetime - curr_datetime
delay=time_diff.total_seconds()

if delay<0:
    print("Time has passed")
else:
    print(f"Time left: {delay} seconds")
    time.sleep(delay)


    send_whatsapp_message(number, message)
