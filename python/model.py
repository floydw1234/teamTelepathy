import numpy as np
import correlation as cor
import MySQLdb 
#import modelAli as ali
db = MySQLdb.connect(host = "127.0.0.1",user="gallery",passwd="eecs118",db="test")
cur = db.cursor()
#WEIGHT = [0.02,0.476,0.377,0.26,1]
#WEIGHT = [0.31,0.61,0.45,0.79,1]
#WEIGHT = [0.29,1,0.42,0.973,0.255] #best for 7 trial (0.67)
#WEIGHT = [0.08,0.94,0.182,1,0.095] #best for 9 trail (0.61)
#WEIGHT = [0.014,0.59,0.0547,1,0.03]
#WEIGHT = [0.01,0.5,0.05,1,0.03] #best for 10 trail (0.65)
#WEIGHT = [0.01,1,0.042,0.0006,0.0002] #300 300 30
#WEIGHT = [0.023,1,0.097,0.0004,0.0009]
#WEIGHT = [0.05,1,0.03,0.0001,0.0007]
WEIGHT = [0.0008,1,0.0003,0,0]
LENGTH = 250
RESPONSE = 350
OFFSETMAX = 45
trailnum = 13

cur.execute("select theta,alpha,low_beta,high_beta,gamma from eeg_avg where person = 'Xiaoyan' order by time asc")
xiaoyanAVG = np.asarray(cur.fetchall())

cur.execute("select theta,alpha,low_beta,high_beta,gamma from eeg_avg where person = 'Jingwei' order by time asc")
jingweiAVG = np.asarray(cur.fetchall())

cur.execute("select theta,alpha,low_beta,high_beta,gamma from eeg_avg where person = 'William' order by time asc")
williamAVG = np.asarray(cur.fetchall())

cur.execute("select theta,alpha,low_beta,high_beta,gamma from eeg_avg where person = 'Ali' order by time asc")
aliAVG = np.asarray(cur.fetchall())

avgEEGDict = {'ali':aliAVG,'jingwei':jingweiAVG,'william':williamAVG,'xiaoyan':xiaoyanAVG}
'''
#This part is for predict
cur.execute("select theta,alpha,low_beta,high_beta,gamma from eeg_repeattime where person = 'Ali' and trials = 11 order by time asc")
testRAW = np.asarray(cur.fetchall())
max = 0
maxPerson = ""
for key in avgEEGDict.keys():
	avg = avgEEGDict[key][RESPONSE:RESPONSE+LENGTH,:]
	result = cor.maxCorrelation(testRAW,avg,response = RESPONSE, length = LENGTH,offset = OFFSETMAX)
	weightedResult = result[0]*np.array(WEIGHT)
	score = sum(weightedResult)
	if score>max:
		max = score
		maxPerson = key
print(maxPerson)


'''
#This part is for training
xiaoyanRAW = [[]] * trailnum
jingweiRAW = [[]] * trailnum
williamRAW = [[]] * trailnum
aliRAW = [[]] * trailnum

for idx in range(0,trailnum):
	cur.execute("select theta,alpha,low_beta,high_beta,gamma from eeg_repeattime where person = 'Xiaoyan' and trials = %s order by time asc",(idx+1,))
	xiaoyanRAW[idx] = np.asarray(cur.fetchall())
	
	cur.execute("select theta,alpha,low_beta,high_beta,gamma from eeg_repeattime where person = 'Jingwei' and trials = %s order by time asc",(idx+1,))
	jingweiRAW[idx] = np.asarray(cur.fetchall())

	cur.execute("select theta,alpha,low_beta,high_beta,gamma from eeg_repeattime where person = 'William' and trials = %s order by time asc",(idx+1,))
	williamRAW[idx] = np.asarray(cur.fetchall())

	cur.execute("select theta,alpha,low_beta,high_beta,gamma from eeg_repeattime where person = 'Ali' and trials = %s order by time asc",(idx+1,))
	aliRAW[idx] = np.asarray(cur.fetchall())

allEEGDict = {'ali':aliRAW,'jingwei':jingweiRAW,'william':williamRAW,'xiaoyan':xiaoyanRAW}
'''
decentRate = 0.05
for trainCount in range(10):
	for i in range(trailnum):
		for k1 in avgEEGDict.keys():
			avg = avgEEGDict[k1][RESPONSE:RESPONSE+LENGTH,:]
			scoreDict = dict()
			for k2 in allEEGDict.keys():
				raw = allEEGDict[k2][i]
				result = cor.maxCorrelation(raw,avg,response = RESPONSE, length = LENGTH,offset = OFFSETMAX)
				weightedResult = result[0]*np.array(WEIGHT)
				score = []
				score.append(weightedResult)
				score.append(sum(weightedResult))
				scoreDict[k2] = score
			correct = scoreDict[k1]
			loss = [0]*5
			for k3 in scoreDict.keys():
				if k1 != k3 :
					for j in range(5):
						#if scoreDict[k3][0][j] > correct[0][j]:
						loss[j] += scoreDict[k3][0][j] - correct[0][j]
			for k in range(5):
				WEIGHT[k] -= decentRate * loss[k]
print(str(WEIGHT))

for i in range(5):
	WEIGHT[i] = round(WEIGHT[i],3)
'''
ofile = open("output.txt","wb")
total = 0
correctTest = 0
for k1 in avgEEGDict.keys():
	avg = avgEEGDict[k1][RESPONSE:RESPONSE+LENGTH,:]
	for i in range(trailnum):
		resultDict = dict()
		for k2 in allEEGDict.keys():
			raw = allEEGDict[k2][i]
			result = cor.maxCorrelation(raw,avg,response = RESPONSE, length = LENGTH,offset = OFFSETMAX)
			result[0] = result[0]*np.array(WEIGHT)
			result.append(round(sum(result[0]),3))	
			resultDict[k2] = result[2]
			message = "The correlation between "+ k1 + " and " + k2 + " for trial " + str(i+1) + " is: " + str(result)+"\n"
			#result = ali.difference_rating(raw,avg)
			#message = "The difference between "+ k1 + " and " + k2 + " for trial " + str(i+1) + " is: " + str(result)+"\n"
			ofile.write(message)
		max = 0
		maxPerson = ""
		for j in resultDict.keys():
			if resultDict[j] > max:
				max = resultDict[j]
				maxPerson = j
		#print("predict person: "+maxPerson+"; correct person: "+k1)
		total += 1
		if maxPerson == k1:
			correctTest += 1
		ofile.write("\n")
	ofile.write("\n")
ofile.close()
print("The accuracy is: "+str(correctTest/float(total)))
