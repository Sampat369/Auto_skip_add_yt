import numpy as np
import os
import pyautogui
import time
import keyboard
import pytesseract
import cv2
t=True
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


region = (0, 500, 450, 450)

ad_active = False
while True:

    # Take screenshot of region 
    screenshot = pyautogui.screenshot(region=region)

    # Convert to OpenCV format
    img = np.array(screenshot)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Optional: improve OCR accuracy
    _, img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

    # Extract text
    text = pytesseract.image_to_string(img).lower()

    # Detect "ad"
    if any(word in text for word in ["download", "sponsored", "visit site","play now", "learn more", "sign up"]):
        print("Ad detected (OCR)")
        ad_active = True
    else:
        ad_active = False
        print("No ad detected (OCR)")
    
    if ad_active:
          pyautogui.hotkey('shift', 'n')
          time.sleep(0.1)
          pyautogui.hotkey('shift', 'p')
          print("Code executed")


    time.sleep(0.1)

    #if the above code is not working or the text is not being detected properly, you can try to increase the region size or adjust the thresholding parameters for better OCR results. 
    #OR remove the continue command and if ad apears on the screen in you tube then press m and n together to execute the code to skip the ad.If still appears then press m and n together again to skip the ad.
    
    continue
    if keyboard.is_pressed('m') and keyboard.is_pressed('n') and t:
            pyautogui.hotkey('shift', 'n')
            time.sleep(0.1)
            pyautogui.hotkey('shift', 'p')
            print("Code executed")
            t=False
    else:
          t=True

   
#python skip_add_yt.py