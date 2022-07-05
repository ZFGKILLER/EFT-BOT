from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32gui
import pydirectinput






while True:
    if pyautogui.locateOnScreen('play.png', grayscale=True, confidence=0.8) != None:
        location = pyautogui.locateOnScreen('play.png')
        pyautogui.click(location)
        time.sleep(1)
        print("launching game")
    
    if pyautogui.locateOnScreen('eftmenu.png', grayscale=True, confidence=0.5) != None:
        pydirectinput.click(971, 646)
        time.sleep(0.5)
     
    if pyautogui.locateOnScreen('pmc.png', grayscale=True, confidence=0.5) != None:
        pydirectinput.click(958, 946)
        time.sleep(0.5)
#maps
    if pyautogui.locateOnScreen('woods.png', grayscale=True, confidence=0.7) != None:
        pydirectinput.click(638, 341)
        time.sleep(1)
        pydirectinput.click(1255, 1018)

    #if pyautogui.locateOnScreen('woods.png', grayscale=True, confidence=0.7) != None:
        #pydirectinput.click(638, 341)
        #time.sleep(1)
        #pydirectinput.click(1255, 1018)
        
    #if pyautogui.locateOnScreen('interchange.png', grayscale=True, confidence=0.7) != None:
        #pydirectinput.click(959, 298)
        #time.sleep(1)
        #pydirectinput.click(1255, 1018)
        
    #if pyautogui.locateOnScreen('customs.png', grayscale=True, confidence=0.7) != None:
        #pydirectinput.click(867, 358)
        #time.sleep(1)
        #pydirectinput.click(1255, 1018)

    #if pyautogui.locateOnScreen('factory.png', grayscale=True, confidence=0.7) != None:
        #pydirectinput.click(732, 441)
        #time.sleep(1)
        #pydirectinput.click(1255, 1018)

    #if pyautogui.locateOnScreen('reserve.png', grayscale=True, confidence=0.7) != None:
        #pydirectinput.click(584, 512)
        #time.sleep(1)
        #pydirectinput.click(1255, 1018)

    #if pyautogui.locateOnScreen('lighthouse.png', grayscale=True, confidence=0.7) != None:
        #pydirectinput.click(557, 626)
        #time.sleep(1)
        #pydirectinput.click(1255, 1018)

    #if pyautogui.locateOnScreen('shoreline.png', grayscale=True, confidence=0.7) != None:
        #pydirectinput.click(668, 712)
        #time.sleep(1)
        #pydirectinput.click(1255, 1018)
#maps finished
    if pyautogui.locateOnScreen('8min.png', grayscale=True, confidence=1) != None:
         print("time exceded")
         pydirectinput.click(956, 1015)
         time.sleep(0.5)
         
    if pyautogui.locateOnScreen('leaving.png', grayscale=True, confidence=0.8) != None:
        print("leaving match time limit was exceeded")
        time.sleep(0.5)
                
    if pyautogui.locateOnScreen('deploying.png', grayscale=True, confidence=0.7) != None:
         print("deploying")
         time.sleep(0.5)

    if pyautogui.locateOnScreen('ac-connectionlost.png', grayscale=True, confidence=0.7) != None:
         print("anti cheat connection lost game must restart")
         pydirectinput.click(962, 580)
         time.sleep(0.5)
    
    if pyautogui.locateOnScreen('connectionlost.png', grayscale=True, confidence=0.7) != None:
         print("connection lost")
         pydirectinput.click(962, 580)
         time.sleep(0.5)

    if pyautogui.locateOnScreen('reconect.png', grayscale=True, confidence=0.7) != None:
         print("connection lost")
         time.sleep(0.2)
         pydirectinput.click(947, 643)

    if pyautogui.locateOnScreen('warningconect.png', grayscale=True, confidence=0.8) != None:
         print("connection lost attempting to recconect")
         time.sleep(1)
         pydirectinput.click(958, 901)
    
    if pyautogui.locateOnScreen('deploy_wait.png', grayscale=True, confidence=0.6) != None:
         print("deploying soon")
         time.sleep(0.5)

    if pyautogui.locateOnScreen('lowstam.png', grayscale=True, confidence=0.9) != None:
                print("stamina low waiting to recoop")
                #prevent any bot
                time.sleep(20)

    if pyautogui.locateOnScreen('failedtofindraid.png', grayscale=True, confidence=0.8) != None:
         print("error failed to find raid, trying again")
         time.sleep(1)
         pydirectinput.click(958, 567)

    if pyautogui.locateOnScreen('bush.png', grayscale=True, confidence=0.9) != None:
                print("bush detected attempting to move away")
                #run avoid bush
                pydirectinput.keyDown('w')
                time.sleep(3)
                pydirectinput.keyUp('w')
                
    
    if pyautogui.locateOnScreen('ingame.png', grayscale=True, confidence=0.45) != None:
                print("in game")
                #run afk bot
                pydirectinput.moveTo(5, 540)
                pydirectinput.keyDown('w')
                time.sleep(0.2)
                pydirectinput.keyDown('shift')
                time.sleep(10)
                pydirectinput.keyUp('shift')
                pydirectinput.keyUp('w')
                time.sleep(1)
                pydirectinput.moveTo(965, 540)
                time.sleep(1.3)
                pydirectinput.keyDown('w')
                time.sleep(0.2)
                pydirectinput.keyDown('shift')
                time.sleep(10)
                pydirectinput.keyUp('shift')
                pydirectinput.keyUp('w')
                time.sleep(1.3)

                
    if pyautogui.locateOnScreen('dead.png', grayscale=True, confidence=0.7) != None:
                print("died or mia")
                pydirectinput.click(958, 946)
                time.sleep(0.5)
                pydirectinput.click(958, 946)
                time.sleep(0.5)
                pydirectinput.click(958, 946)
                time.sleep(0.5)
                pydirectinput.click(958, 946)
                time.sleep(0.5)
                #heal
                #pydirectinput.click(1285, 965)
                #time.sleep(0.5)
                #heal
                pydirectinput.click(958, 946)
                time.sleep(0.5)

            
                   
