#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:27:59 2020

@author: milind
"""

import pyttsx3 

engine=pyttsx3.init()

def speech_init(): # Initialises Speech Output
    engine.setProperty('rate', 150)
    engine.setProperty('volume' , 1)
    voices=engine.getPropertyvoices = engine.getProperty('voices')       
    engine.setProperty('voice', voices[0].id)
    pass
    
def speech_output(x): # Is the Speech Output Function
    
    engine.say(x)
    engine.runAndWait()
    pass

def open_website(a): # Function To open Webbrowser
    import  webbrowser

    a = ""

    webbrowser.get("chrome").open_new_tab(a)

    pass

    """ Main Code """
    
speech_init()

print("I am Covexa your Corona HelpBot")
x="i am covexa , your corona help bot"
speech_output(x)

print("Ask Any Question")

print("To exit enter Z")  
  
userinp=input("Enter your question ").lower()

while True :
    
    if "corona" in userinp :
        x="It is a new virus"
        speech_output(x)
        userinp=input("Enter your question ").lower()
    if "precaution" in userinp :
        x="Quarantine yourselves if having symptoms or in infected area "
        speech_output(x)
        a="https://www.who.int"
        open_website(a)
        userinp=input("Enter your question ").lower()
        
    
    if "transmission" in userinp :
        x='covid nineteen transmits through droplets '
        speech_output(x)
        userinp=input("Enter your question ").lower()
    
    if "origin" in userinp :
        x="Wuhan, Hubei Province ,China"
        speech_output(x)
        userinp=input("Enter your question ").lower()
        
    if "symptoms " in userinp :
        x='symptoms of corona include cough, fever,etc'
        speech_output(x)
        userinp=input("Enter your question ").lower()
        
    if "updates" in userinp :
        a="https://www.who.int"
        open_website(a)
        userinp=input("Enter your question ").lower()
    
    if "sanitizer " in userinp :
        x='use alcoholic hand sanitizer'
        speech_output(x) 
        userinp=input("Enter your question ").lower()
        
    if "z" in userinp :
        break

x="Hope you are well"
speech_output(x)

print("See you later")  



      
   
        
    
    
        
            
    
    
        
    