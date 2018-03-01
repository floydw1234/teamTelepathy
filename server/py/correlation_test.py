import numpy as np
import correlation as cor
import MySQLdb 
db = MySQLdb.connect(host = "127.0.0.1",user="gallery",passwd="eecs118",db="eeg_db")
cur = db.cursor()
LENGTH = 400
RESPONSE = 200
trailnum = 2
xiaoyanEEG = [] * trailnum
xiaoyanRAW = [] * trailnum
jingweiEEG = [] * trailnum
jingweiRAW = [] * trailnum
williamEEG = [] * trailnum
williamRAW = [] * trailnum
aliEEG = [] * trailnum
aliRAW = [] * trailnum

for idx in range(trailnum):
	cur.execute("select theta,alpha,low_beta,high_beta,gamma from eeg_raw where person = 'Xiaoyan' and trial = %s",(idx+1,))
	xiaoyanEEG.append(cur.fetchall())
	xiaoyanRAW.append(np.asarray(xiaoyanEEG[idx]))

	cur.execute("select theta,alpha,low_beta,high_beta,gamma from eeg_raw where person = 'Jingwei' and trial = %s",(idx+1,))
	jingweiEEG.append(cur.fetchall())
	jingweiRAW.append(np.asarray(jingweiEEG[idx]))

	cur.execute("select theta,alpha,low_beta,high_beta,gamma from eeg_raw where person = 'William' and trial = %s",(idx+1,))
	williamEEG.append(cur.fetchall())
	williamRAW.append(np.asarray(williamEEG[idx]))

	cur.execute("select theta,alpha,low_beta,high_beta,gamma from eeg_raw where person = 'Ali' and trial = %s",(idx+1,))
	aliEEG.append(cur.fetchall())
	aliRAW.append(np.asarray(aliEEG[idx]))

allEEGDict = {'ali':aliRAW,'jingwei':jingweiRAW,'william':williamRAW,'xiaoyan':xiaoyanRAW}
ofile = open("output.txt","wb")
for k1 in allEEGDict.keys():
	data = allEEGDict[k1][0]
	avg_eeg = allEEGDict[k1][1][RESPONSE:RESPONSE+LENGTH,:]
	result = cor.maxCorrelation(data,avg_eeg)
	message = "\nThe correlation between trail 1 and trail 2 for " + k1 + " is: " + str(result)+"\n"
	ofile.write(message)
	for k2 in allEEGDict.keys():
		if k1 != k2:
			for i in range(trailnum):
				data = allEEGDict[k1][i]
				avg_eeg = allEEGDict[k2][i][RESPONSE:RESPONSE+LENGTH,:]
				result = cor.maxCorrelation(data,avg_eeg)
				message = "The correlation between "+ k1 + " and " + k2 + " for trial " + str(i+1) + " is: " + str(result)+"\n"
				ofile.write(message)
				
ofile.close()
			