from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32gui
import pydirectinput






while True:
    if pyautogui.locateOnScreen('EFTMENU.png', grayscale=True, confidence=0.5) != None:
        pyautogui.click(971, 646)
        time.sleep(0.5)
     
    if pyautogui.locateOnScreen('PMC.png', grayscale=True, confidence=0.5) != None:
        pyautogui.click(958, 946)
        time.sleep(0.5)
#maps
    if pyautogui.locateOnScreen('WOODS.png', grayscale=True, confidence=0.7) != None:
        pyautogui.click(638, 341)
        time.sleep(1)
        pyautogui.click(1255, 1018)

    #if pyautogui.locateOnScreen('WOODS.png', grayscale=True, confidence=0.7) != None:
        #pyautogui.click(638, 341)
        #time.sleep(1)
        #pyautogui.click(1255, 1018)
        
    #if pyautogui.locateOnScreen('INTERCHANGE.png', grayscale=True, confidence=0.7) != None:
        #pyautogui.click(959, 298)
        #time.sleep(1)
        #pyautogui.click(1255, 1018)
        
    #if pyautogui.locateOnScreen('CUSTOMS.png', grayscale=True, confidence=0.7) != None:
        #pyautogui.click(867, 358)
        #time.sleep(1)
        #pyautogui.click(1255, 1018)

    #if pyautogui.locateOnScreen('FACTORY.png', grayscale=True, confidence=0.7) != None:
        #pyautogui.click(732, 441)
        #time.sleep(1)
        #pyautogui.click(1255, 1018)

    #if pyautogui.locateOnScreen('RESERVE.png', grayscale=True, confidence=0.7) != None:
        #pyautogui.click(584, 512)
        #time.sleep(1)
        #pyautogui.click(1255, 1018)

    #if pyautogui.locateOnScreen('LIGHTHOUSE.png', grayscale=True, confidence=0.7) != None:
        #pyautogui.click(557, 626)
        #time.sleep(1)
        #pyautogui.click(1255, 1018)

    #if pyautogui.locateOnScreen('SHORELINE.png', grayscale=True, confidence=0.7) != None:
        #pyautogui.click(668, 712)
        #time.sleep(1)
        #pyautogui.click(1255, 1018)
#maps finished
    if pyautogui.locateOnScreen('8MIN.png', grayscale=True, confidence=1) != None:
         print("Time exceded")
         pyautogui.click(956, 1015)
         time.sleep(0.5)
         
    if pyautogui.locateOnScreen('LEAVING.png', grayscale=True, confidence=0.8) != None:
        print("LEAVING MATCH TIME LIMIT WAS EXCEEDED")
        time.sleep(0.5)
                
    if pyautogui.locateOnScreen('DEPLOYING.png', grayscale=True, confidence=0.7) != None:
         print("DEPLOYING")
         time.sleep(0.5)

    if pyautogui.locateOnScreen('CONNECTIONLOST.PNG', grayscale=True, confidence=0.7) != None:
         print("CONNECTION LOST")
         pyautogui.click(962, 580)
         time.sleep(0.5)

    if pyautogui.locateOnScreen('RECONECT.png', grayscale=True, confidence=0.7) != None:
         print("Connection Lost")
         time.sleep(0.2)
         pyautogui.click(947, 643)

    if pyautogui.locateOnScreen('WARNINGCONECT.png', grayscale=True, confidence=0.8) != None:
         print("Connection Lost Attempting To Recconect")
         time.sleep(1)
         pyautogui.click(958, 901)
    
    if pyautogui.locateOnScreen('DEPLOY_WAIT.png', grayscale=True, confidence=0.6) != None:
         print("DEPLOYING IN")
         time.sleep(0.5)

    if pyautogui.locateOnScreen('LOWSTAM.png', grayscale=True, confidence=0.9) != None:
                print("LOW STAM")
                #prevent any bot
                time.sleep(20)

    if pyautogui.locateOnScreen('BUSH.png', grayscale=True, confidence=0.9) != None:
                print("BUSH DETECTED")
                #run avoid bush
                pyautogui.keyDown('w')
                time.sleep(3)
                pyautogui.keyUp('w')
                
    
    if pyautogui.locateOnScreen('INGAME.png', grayscale=True, confidence=0.6) != None:
                print("IN GAME")
                #run afk bot
                pydirectinput.moveTo(5, 540)
                pyautogui.keyDown('w')
                time.sleep(0.2)
                pydirectinput.keyDown('shift')
                time.sleep(10)
                pydirectinput.keyUp('shift')
                pyautogui.keyUp('w')
                time.sleep(1)
                pydirectinput.moveTo(965, 540)
                time.sleep(1.3)
                pyautogui.keyDown('w')
                time.sleep(0.2)
                pydirectinput.keyDown('shift')
                time.sleep(10)
                pydirectinput.keyUp('shift')
                pyautogui.keyUp('w')
                time.sleep(1.3)

                
    if pyautogui.locateOnScreen('DEAD.png', grayscale=True, confidence=0.7) != None:
                print("DIED OR MIA")
                pyautogui.click(958, 946)
                time.sleep(0.5)
                pyautogui.click(958, 946)
                time.sleep(0.5)
                pyautogui.click(958, 946)
                time.sleep(0.5)
                pyautogui.click(958, 946)
                time.sleep(0.5)
                #heal
                #pyautogui.click(1285, 965)
                #time.sleep(0.5)
                #heal
                pyautogui.click(958, 946)
                time.sleep(0.5)
                
