import time
from datetime import datetime
from plyer import notification
                # MONTH - DATE
birthdates = { 
              "Name1":"02-21"
            }

while True:
    
    d = datetime.today()

    for  name in birthdates:
        bdate = birthdates[name]
        month = int(bdate[0:2])
        date = int(bdate[3:5])  
         
        if(month==d.month):
            
            if(date==d.day):
                
                fmessage = "TODAY   IS   " + name + "  'S    BIRTHDAY" 
                notification.notify(message=fmessage,app_icon="BIRTHDAY_ICON.ico",timeout=10)
                time.sleep(43200)
