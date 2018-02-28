import sys
import os
import os.path
import platform
import time
import ctypes
import csv
import time
import threshold


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

# -------------------------------------------------------------------------
print "==================================================================="
print "Example to get the average band power for a specific channel from" \
" the latest epoch."
print "==================================================================="

# -------------------------------------------------------------------------
if libEDK.IEE_EngineConnect("Emotiv Systems-5") != 0:
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
tempTime = round(time.time()*1000)
measureTime = 0
firsttimeflag=0

testPerson = sys.argv[1]
cur.execute("select max(trials) from eeg_raw where person = %s",(testPerson,))
trailnumber = 0
data = cur.fetchall()
for row in data:
	if not row[0]:
		break
	trailnumber = row[0]
trailnumber = trailnumber+1
counter=0

while (measureTime <= 20000):
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

                    if firsttimeflag==0:
                        firsttimeflag=1
                        tempTime = round(time.time()*1000)
                        print tempTime
                    timeDB = round(time.time()*1000) - tempTime
                    thetaDB = thetaValue.value
                    alphaDB = alphaValue.value
                    low_betaDB = low_betaValue.value
                    high_betaDB = high_betaValue.value
                    gammaDB = gammaValue.value

                    print counter
                    print trailnumber
                    cur.execute("INSERT INTO eeg_raw (time, theta, alpha, low_beta, high_beta, gamma,trials, person) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(counter, thetaDB, alphaDB, low_betaDB, high_betaDB, gammaDB,trailnumber,testPerson))
                    db.commit()

                    if trailnumber==1:
                        if (counter<500 and counter>=350):
                            cur.execute("INSERT INTO eeg_avg (time, theta, alpha, low_beta, high_beta, gamma,trials, person) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(counter, thetaDB, alphaDB, low_betaDB, high_betaDB, gammaDB,trailnumber,testPerson))
                            db.commit()

                    print >> f, round(time.time()*1000) - tempTime,', ',
                    print >> f, thetaValue.value,', ',
                    print >> f, alphaValue.value, ', ',
                    print >> f, low_betaValue.value, ', ',
                    print >> f, high_betaValue.value, ', ',
                    print >> f, gammaValue.value, ', \n',


                    counter=counter+1
                    #print "%.6f, %.6f, %.6f, %.6f, %.6f \n" % (thetaValue.value, alphaValue.value,
                    #                                          low_betaValue.value, high_betaValue.value, gammaValue.value)

    elif state != 0x0600:
        print "Internal error in Emotiv Engine ! "
    time.sleep(0.1)
    measureTime = round(time.time()*1000) - tempTime

if(trailnumber>1):
    person=[]
    cur.execute("select * from eeg_raw where person = %s and trials=%s",(testPerson,trailnumber,))

    data = cur.fetchall()
    for row in data:
            person.append(row)

    old_ave=[]
    cur.execute("select * from eeg_avg where person = %s",(testPerson,))
    data = cur.fetchall()
    for row in data:
            old_ave.append(row)

    new_ave=[]
    new_ave=threshold.new_avg(person, old_ave)

    print new_ave
    cur.execute("drop table if exists `eeg_avg`")
    db.commit()
    cur.execute("CREATE TABLE `eeg_avg` (\
                `time` int(10) NOT NULL,\
                `theta` float(10) DEFAULT NULL,\
                `alpha` float(10) DEFAULT NULL,\
                `low_beta` float(10) DEFAULT NULL,\
                `high_beta` float(10) DEFAULT NULL,\
                `gamma` float(10) DEFAULT NULL,\
                `trials` int(5) not null,\
                `person` char(20) not null\
                )")
    db.commit()
    for i in range (150):
        cur.execute("INSERT INTO eeg_avg(time, theta, alpha, low_beta, high_beta, gamma,trials, person ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(new_ave[i+1][0], new_ave[i+1][1], new_ave[i+1][2], new_ave[i+1][3], new_ave[1+i][4], new_ave[i+1][5],new_ave[i+1][6],new_ave[i+1][7]))
        db.commit()

#print person
#print old_ave
#print new_ave
# -------------------------------------------------------------------------
libEDK.IEE_EngineDisconnect()
libEDK.IEE_EmoStateFree(eState)
libEDK.IEE_EmoEngineEventFree(eEvent)

#db.close()

'''
f = open('E:/Study/community-sdk-master/examples_basic/Python/raw_eeg1.txt', 'w')
f.write("Hello World!")
f.close()'''
