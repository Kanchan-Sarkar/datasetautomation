#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pyautogui
import time

with pyautogui.hold('win'):
    pyautogui.press('r')
    
pyautogui.write('Chrome')
time.sleep(1)
pyautogui.press('enter')

pyautogui.moveTo(270,62)
pyautogui.leftClick()
pyautogui.write('kaggle.com')
pyautogui.press('enter')
time.sleep(2)
pyautogui.moveTo(1472,128)
time.sleep(1)
pyautogui.leftClick()
time.sleep(2)
pyautogui.write('Heart Failure Prediction')
time.sleep(2)
pyautogui.press('enter')
time.sleep(1)
pyautogui.moveTo(736, 497)
pyautogui.leftClick()
time.sleep(2)
pyautogui.moveTo(1592,236)
time.sleep(1)
pyautogui.leftClick()
time.sleep(3)

pyautogui.moveTo(19,65)
pyautogui.leftClick()
time.sleep(1)
pyautogui.moveTo(736, 497)

for i in range(4):
    pyautogui.scroll(-300)
    
pyautogui.leftClick()
time.sleep(2)
pyautogui.moveTo(1598,236)
pyautogui.leftClick()
time.sleep(3)

pyautogui.moveTo(19,65)
for i in range(4):
    pyautogui.leftClick()


# In[ ]:




