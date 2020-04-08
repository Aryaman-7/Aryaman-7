#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:27:59 2020

@author: milind
"""

import pyttsx3 

engine=pyttsx3.init()

def speech_init():
    engine.setProperty('rate', 125)
    engine.setProperty('volume' , 1)
    voices=engine.getPropertyvoices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[0].id)
    pass
    
def speech_output(x):
    x="a"
    engine.say(x)
    engine.runAndWait()
    pass

def open_website(a):
    import  webbrowser

    a = ""

    webbrowser.get("chrome").open_new_tab(a)

    pass

    """ Main Code """
    
speech_init()
    
userinp=input("Enter your question ").lower()
print("To exit enter Z")
while True :
    if "corona" in userinp :
        x="It is a new virus"
        speech_output(x)
    
    if 'precaution' in userinp :
        x="Quarantine yourselves if having symptoms or in infected area "
        speech_output(x)
        a="https://www.who.int"
        open_website(a)
        
        
    
    if 'transmission' in userinp :
        x='covid nineteen transmits through droplets '
        speech_output(x)

    
    if 'origin' in userinp :
        x="Wuhan, Hubei Province ,China"
        speech_output(x)
        
    if 'symptoms ' in userinp :
        x='symptoms of corona include cough, fever,etc'
        speech_output(x)
        
        
    if 'updates' in userinp :
        a="https://www.who.int"
        open_website(a)
        
    
    if 'santizer ' in userinp :
        x='use alcoholic hand sanitizer'
        speech_output(x) 
        
    if "z " in userinp :
        break

print("Hope you are well")
print("See you later")  

engine.say ("see you later")
engine.runAndWait()
engine.stop()
      
   
        
    
    
        
            
    
    
        
    