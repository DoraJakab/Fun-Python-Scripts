import pyautogui as pt
import time

def nav_to_image(image, clicks, off_x=0, off_y=0):
    position = pt.locateCenterOnScreen(image, confidence=.5) # locate and recognise with 50% confidence

    if position is None:
        print(f'{image} not found...')
        return 0
    else:
        pt.moveTo(position, duration=.1)
        pt.moveRel(off_x, off_y, duration=.1)
        pt.click(clicks=clicks, interval=.3)

def teams(images, clicks, off_x=0, off_y=0):
    for image in images:
        position = pt.locateCenterOnScreen(image, confidence=0.5)
        if position is None:
            print(f'{image} not found...')
            return 0
        else:
            pt.moveTo(position, duration=.1)
            pt.moveRel(off_x, off_y, duration=.1)
            pt.click(clicks=clicks, interval=.3)

time.sleep(2)

images = [r'C:\Work\FDM\Python\Typewriter\teams.PNG', r'C:\Work\FDM\Python\Typewriter\teams1.PNG'] # list of the image paths

teams(images, 1) # find teams icon

# nav_to_image(r'C:\Work\FDM\Python\Typewriter\teams.PNG', 1)

nav_to_image(r'C:\Work\FDM\Python\Typewriter\tab.PNG', 1) # find chat category

nav_to_image(r'C:\Work\FDM\Python\Typewriter\chat.PNG', 1) # find chat

#nav_to_image(r'C:\Work\FDM\Python\Typewriter\box.PNG', 1) # find chatbox

pt.typewrite("Script test...", interval=0.1)
pt.press('enter')