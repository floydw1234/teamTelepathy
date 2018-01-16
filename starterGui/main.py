import sys
import os
import platform
import time
import ctypes
import easygui as g
import webbrowser


weHaveValues = False

while (1):
    # start of easygui stuff
    msg = "Enter Your username to start training"
    title = "EEG Identifier Training Gui"
    fieldNames = ["UserName"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = g.multenterbox(msg,title, fieldNames)
    if fieldValues == None:
        break
    errmsg = ""
    for i in range(len(fieldNames)):
      if fieldValues[i].strip() == "":
        errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
    if errmsg == "":
        break # no problems found
    fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)

tempTime = time.time()

while(time.time() - tempTime < 4):
    print time.time()
    cont = g.ccbox(msg='Shall I continue?', title=' ', choices=('C[o]ntinue', 'C[a]ncel'), image="black.jpg", default_choice='Continue', cancel_choice='Cancel')
    #end of easygui stuff
    if weHaveValues == True:
        storeValues(user,theta,alpha,Lbeta,Hbeta,gamma)

tempTime = time.time()

while(time.time() - tempTime < 4):
    cont = g.ccbox(msg='Shall I continue?', title=' ', choices=('C[o]ntinue', 'C[a]ncel'), image="smeadly.jpg", default_choice='Continue', cancel_choice='Cancel')
    #end of easygui stuff
    if weHaveValues == True:
        storeValues(user,theta,alpha,Lbeta,Hbeta,gamma)

def storeValues(user,theta,alpha,Lbeta,Hbeta,gamma):
    '''
    fill this in with communications with the database
    '''
