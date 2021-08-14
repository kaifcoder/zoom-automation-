import subprocess
import time
import pyautogui
import pandas as pd
from datetime import datetime

def sign_in(meetingid, pswd):
    subprocess.call(r"C:\Users\Kaif\AppData\Roaming\Zoom\bin\Zoom.exe")     #give the path of zoom application here 

    time.sleep(5)

    join_btn = pyautogui.locateCenterOnScreen('join_button.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    meeting_id_btn =  pyautogui.locateCenterOnScreen('meeting_id_button.png')
    pyautogui.moveTo(meeting_id_btn)
    pyautogui.click()
    
    pyautogui.write(meetingid,interval=0.1)
    
    media_btn = pyautogui.locateAllOnScreen('media_btn.png')
    for btn in media_btn:
        pyautogui.moveTo(btn)
        pyautogui.click()
        time.sleep(2)

    join_btn = pyautogui.locateCenterOnScreen('join_btn.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()

    time.sleep(8)
    meeting_pswd_btn = pyautogui.locateCenterOnScreen('meeting_pswd.png')
    time.sleep(2)
    pyautogui.moveTo(meeting_pswd_btn)
    time.sleep(1)
    pyautogui.click()
    pyautogui.write(pswd,interval=0.1)
    pyautogui.press('enter')

    time.sleep(10)
    meeting_got_it_btn = pyautogui.locateCenterOnScreen('got_it_btn.png')
    time.sleep(2)
    pyautogui.moveTo(meeting_got_it_btn)
    time.sleep(1)
    pyautogui.click()

    time.sleep(20)
    time.sleep(10)
    pyautogui.hotkey('alt','h')
    pyautogui.write('CS_0075_MOHD KAIF',interval=0.1)     #just type your name here with roll no 
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('alt','h')
    

df = pd.read_csv('timings.csv')

while True:
    # checking of the current time exists in our csv file
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):

       row = df.loc[df['timings'] == now]
       m_id = str(row.iloc[0,1])
       m_pswd = str(row.iloc[0,2])
       
       sign_in(m_id,m_pswd)
       time.sleep(20)
       print('signed in')
