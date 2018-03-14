import sys
import os
import os.path
import platform
import time
import ctypes
import csv
import time
import threshold
import numpy as np
import correlation as cor


from array import *
from ctypes import *
from __builtin__ import exit

#connect MySQL
import MySQLdb


db = MySQLdb.connect(host = "127.0.0.1",user="gallery",passwd="eecs118",db="eeg_db")
cur = db.cursor()
#a = 1
#b = 'xiaoyan'
#cur.execute("INSERT INTO eeg_raw (trail, person, time, theta, alpha, low_beta, high_beta, gamma) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(a,b,a,a,a,a,a,a))
#db.commit()
#print "finish"
'''
if sys.platform.startswith('win32'):
    import msvcrt
elif sys.platform.startswith('linux'):
    import atexit
    from select import select

from ctypes import *

try:
    if sys.platform.startswith('win32'):
        libEDK = cdll.LoadLibrary("edk.dll")
    else:
        raise Exception('System not supported.')
except Exception as e:
    print 'Error: cannot load EDK lib:', e
    exit()

IEE_EmoEngineEventCreate = libEDK.IEE_EmoEngineEventCreate
IEE_EmoEngineEventCreate.restype = c_void_p
eEvent = IEE_EmoEngineEventCreate()

IEE_EmoEngineEventGetEmoState = libEDK.IEE_EmoEngineEventGetEmoState
IEE_EmoEngineEventGetEmoState.argtypes = [c_void_p, c_void_p]
IEE_EmoEngineEventGetEmoState.restype = c_int

IEE_EmoStateCreate = libEDK.IEE_EmoStateCreate
IEE_EmoStateCreate.restype = c_void_p
eState = IEE_EmoStateCreate()

userID = c_uint(0)
user   = pointer(userID)
ready  = 0
state  = c_int(0)

alphaValue     = c_double(0)
low_betaValue  = c_double(0)
high_betaValue = c_double(0)
gammaValue     = c_double(0)
thetaValue     = c_double(0)

alpha     = pointer(alphaValue)
low_beta  = pointer(low_betaValue)
high_beta = pointer(high_betaValue)
gamma     = pointer(gammaValue)
theta     = pointer(thetaValue)

channelList = array('I',[3, 7, 9, 12, 16])   # IED_AF3, IED_AF4, IED_T7, IED_T8, IED_Pz
'''
# -------------------------------------------------------------------------
#print "==================================================================="

#print "Example to get the average band power for a specific channel from" \
#" the latest epoch."
#print "==================================================================="

# -------------------------------------------------------------------------
'''if libEDK.IEE_EngineConnect("Emotiv Systems-5") != 0:
        print "Emotiv Engine start up failed."
        exit();

print "Theta, Alpha, Low_beta, High_beta, Gamma \n"

i = 0
path = 'csv/raw_eeg'+ '-' +sys.argv[1] + '-' + str(i) +  '.csv'
while(os.path.isfile(path)):
    i += 1
    path = 'csv/raw_eeg'+sys.argv[1] + '-' + str(i) +  '.csv'


f = file(path, 'w')
f = open(path, 'w')
print >> f, "time, theta, alpha, low_beta, high_beta, gamma,\n",
'''
tempTime = round(time.time()*1000)
measureTime = 0
firsttimeflag=0
triallist=[]
thetalist=[]
alphalist=[]
low_betalist=[]
high_betalist=[]
gammalist=[]
testPersonRAW=[]
'''
testPerson = sys.argv[1]
cur.execute("select max(trials) from eeg_raw where person = %s",(testPerson,))
trailnumber = 0
data = cur.fetchall()
for row in data:
    if not row[0]:
        break
    trailnumber = row[0]
trailnumber = trailnumber+1
'''
counter=0

while (measureTime <= 20000):
    '''
    state = libEDK.IEE_EngineGetNextEvent(eEvent)

    if state == 0:
        eventType = libEDK.IEE_EmoEngineEventGetType(eEvent)
        libEDK.IEE_EmoEngineEventGetUserId(eEvent, user)
        if eventType == 16:  # libEDK.IEE_Event_enum.IEE_UserAdded
            ready = 1
            libEDK.IEE_FFTSetWindowingType(userID, 1);  # 1: libEDK.IEE_WindowingTypes_enum.IEE_HAMMING
            print "User added"

        if ready == 1:
            for i in channelList:
                result = c_int(0)
                result = libEDK.IEE_GetAverageBandPowers(userID, i, theta, alpha, low_beta, high_beta, gamma)

                if result == 0:    #EDK_OK
'''
    if firsttimeflag==0:
        firsttimeflag=1
        tempTime = round(time.time()*1000)
#        print tempTime
    timeDB = round(time.time()*1000) - tempTime
    #thetaDB = thetaValue.value
    #alphaDB = alphaValue.value
    #low_betaDB = low_betaValue.value
    #high_betaDB = high_betaValue.value
    #gammaDB = gammaValue.value

#    print counter
   # print trailnumber
   # cur.execute("INSERT INTO eeg_raw (time, theta, alpha, low_beta, high_beta, gamma,trials, person) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(counter, thetaDB, alphaDB, low_betaDB, high_betaDB, gammaDB,trailnumber,testPerson))
   # db.commit()
   # cur.execute("INSERT INTO eeg_raw (time, theta, alpha, low_beta, high_beta, gamma,trials, person) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(counter, 100, 100, 100, 100, 100,trailnumber,testPerson))
   # db.commit()
    ''' triallist.append(counter)
        thetalist.append(thetaDB)
        alphalist.append(alphaDB)
        low_betalist.append(low_betalDB)
        high_betalist.append(high_betaDB)
        gammalist.append(gammaDB)
    '''
    triallist.append(counter)
    thetalist.append(counter)
    alphalist.append(counter)
    low_betalist.append(counter)
    high_betalist.append(counter)
    gammalist.append(counter)


    #if trailnumber==1:
    #    if (counter<500 and counter>=350):
    #        cur.execute("INSERT INTO eeg_avg (time, theta, alpha, low_beta, high_beta, gamma,trials, person) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(counter, 1, 1, 1, 1, 1,trailnumber,testPerson))
    #        db.commit()
            #cur.execute("INSERT INTO eeg_raw (time, theta, alpha, low_beta, high_beta, gamma,trials, person) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(counter, 1, 1, 1, 1, 1,trailnumber,testPerson))
            #db.commit()

    #print >> f, round(time.time()*1000) - tempTime,', ',
    #print >> f, thetaValue.value,', ',
    #print >> f, alphaValue.value, ', ',
    #print >> f, low_betaValue.value, ', ',
    #print >> f, high_betaValue.value, ', ',
    #print >> f, gammaValue.value, ', \n',


    counter=counter+1
    #print "%.6f, %.6f, %.6f, %.6f, %.6f \n" % (thetaValue.value, alphaValue.value,
    #                                          low_betaValue.value, high_betaValue.value, gammaValue.value)

#elif state != 0x0600:
#   print "Internal error in Emotiv Engine ! "
    #time.sleep(0.05)
    measureTime = round(time.time()*1000) - tempTime


testPersonRAW.append(thetalist)
testPersonRAW.append(alphalist)
testPersonRAW.append(low_betalist)
testPersonRAW.append(high_betalist)
testPersonRAW.append(gammalist)
testPersonX = np.array(testPersonRAW)
testPersonX = testPersonX[:,350:500].T
#print testPersonX.shape
LENGTH = 150
RESPONSE = 350
trailnum = 1 #define how many trails you want to include
xiaoyanEEG = [] * trailnum  #EEG: data direct from the database
xiaoyanRAW = [] * trailnum  #RAW: convert EEG data to array form
jingweiEEG = [] * trailnum
jingweiRAW = [] * trailnum
williamEEG = [] * trailnum
williamRAW = [] * trailnum
aliEEG = [] * trailnum
aliRAW = [] * trailnum
for idx in range(trailnum):
    cur.execute("select theta,alpha,low_beta,high_beta,gamma from eeg_raw where person = 'Xiaoyan' and trials = %s",(idx+1,))
    xiaoyanEEG.append(cur.fetchall())
    xiaoyanRAW.append(np.asarray(xiaoyanEEG[idx]))

    cur.execute("select theta,alpha,low_beta,high_beta,gamma from eeg_raw where person = 'Jingwei' and trials = %s",(idx+1,))
    jingweiEEG.append(cur.fetchall())
    jingweiRAW.append(np.asarray(jingweiEEG[idx]))

    cur.execute("select theta,alpha,low_beta,high_beta,gamma from eeg_raw where person = 'William' and trials = %s",(idx+1,))
    williamEEG.append(cur.fetchall())
    williamRAW.append(np.asarray(williamEEG[idx]))

    cur.execute("select theta,alpha,low_beta,high_beta,gamma from eeg_raw where person = 'Ali' and trials = %s",(idx+1,))
    aliEEG.append(cur.fetchall())
    aliRAW.append(np.asarray(aliEEG[idx]))


allEEGDict = {'ali':aliRAW,'jingwei':jingweiRAW,'william':williamRAW,'xiaoyan':xiaoyanRAW}
ofile = open("output.txt","wb")
for k1 in allEEGDict.keys():
    '''
    data = allEEGDict[k1][0]
    avg_eeg = allEEGDict[k1][1][RESPONSE:RESPONSE+LENGTH,:]
    result = cor.maxCorrelation(data,avg_eeg)
    message = "\nThe correlation between trail 1 and trail 2 for " + k1 + " is: " + str(result)+"\n"
    ofile.write(message)
    '''
    for i in range(trailnum):
        data = allEEGDict[k1][i]
        #print data.shape
        avg_eeg = np.asarray(testPersonX)
        result = cor.maxCorrelation(data,avg_eeg)
        message = "The correlation between "+ k1 + " and  new User for trial " + str(i+1) + " is: " + str(result)+"\n"
        ofile.write(message)
print k1