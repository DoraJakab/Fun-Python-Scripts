import pyautogui as pt
import time
from plyer import notification

pt.FAILSAFE = True # always have failsafe on

'''Need to be outside of the teams window to work, otherwise the icon doesn't change'''

def notif(image, check_interval=5): # check every 5 seconds
    while True:
        try:
            position = pt.locateOnScreen(image, confidence=0.9) # check for the Teams notification icon, 90% confidence rate needed
            if position is not None:
                notification.notify(
                    title = 'New Teams Notification',
                    message = 'You have a new teams notification',
                    app_icon = None,
                    timeout = 10
                )
                print('Notification detected')
                break
        except:
            pass # ignore ImageNotFoundException, absolutely necessary otherwise loop will stop after one check
        time.sleep(check_interval)

def nav_to_image(image, clicks, off_x=0, off_y=0):
    position = pt.locateCenterOnScreen(image, confidence=.5) # locate and recognise with 50% confidence

    if position is None:
        print(f'{image} not found...')
        return 0
    else:
        pt.moveTo(position, duration=.1)
        pt.moveRel(off_x, off_y, duration=.1)
        pt.click(clicks=clicks, interval=.3)

image = r'C:\Work\FDM\Python\Typewriter\teams1.PNG' # notification icon path

notif(image)

pt.alert(text = 'You have a new teams notification', title = 'New Teams Notification!!',  button = 'OK') # prints alert on screen once loop is done

nav_to_image(image, 1) # opens teams