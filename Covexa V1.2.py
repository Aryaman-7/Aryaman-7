#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 11:43:47 2020

@author: pallavideshmukh
"""


import pyttsx3
import speech_recognition as speech

engine = pyttsx3.init()

def start_listening():
            
    r = speech.Recognizer() 
    with speech.Microphone() as source:
            r.adjust_for_ambient_noise(source) 
            print("Speak:")
            audio = r.listen(source)
    command=r.recognize_google(audio)
    print("You said" + command)
    return command         


words = start_listening().lower()

if 'hello' in words:    
    engine.say('Hi I am Covexa, your Alexa for the Corona Virus Help  ')
    engine.runAndWait() 

if "sanitizer" in words :
    print ( "You should use an alcoholic hand sanitizer to kill germs")
    engine.say("You should use an alcoholic hand sanitizer to kill germs")
    engine.runAndWait()

if "what" and "corona virus" in words :
    print("It is a new virus that has a mortality rate of 1.38%")
    engine.say("It is a new virus that has a mortality rate of 1.38%")
    engine.runAndWait()
   
if "what" and "symptoms" and "corona virus" in words :
    print ("The symptoms of COVID-19 include dry cough, fever, fatigue,Severe Acute Respiratory Sindrome ,etc")
    engine.say("The symptoms of Covid nineteen include dry cough, fever, fatigue, Severe Acute Respiratory Sindrome, etc")
    engine.runAndWait()
       
       
if "cure" and "corona virus" in words :
    print ("A cure to Corona Virus is not found yet")
    engine.say ("A cure to Corona Virus is not found yet")
    engine.runAndWait()
       
if "prevent" and "corona virus" in words :
    print ("You should always wash your hands with soap and water, you should not restrain from touching things and quarantine yourself if you are ill and if you are in a Corona Virus Affrected area")
    engine.say("You should always wash your hands with soap and water, you should not restrain from touching things and quarantine yourself if you are ill and if you are in a Corona Virus Affrected area")
    engine.runAndWait()
       
if "cases"   and "worldwide"  in words  :
    print ("There are 803547 cases of corona virus worldwide as of 7:20 IST, 31st March,2020")
    engine.say ("There are 803547 cases of corona virus worldwide as of 7:20 IST, 31st March,2020")
    engine.runAndWait()
   
if "cases" and "india" in words :
    print ("There are 1117 cases of Corona Virus in India as of 7:34 IST, 31st March,2020")
    engine.say("There are 1117 cases of Corona Virus in India as of 7:34 IST, 31st March,2020")
    engine.runAndWait()
       
if "bye" in words :
    print("Bye, hope you are well buddy!")
    engine.say("Bye, hope you are well buddy!")
    engine.runAndWait()
    engine.stop()