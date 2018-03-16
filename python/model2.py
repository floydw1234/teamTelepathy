import numpy as np
import correlation as cor
import MySQLdb 
#import modelAli as ali
db = MySQLdb.connect(host = "127.0.0.1",user="gallery",passwd="eecs118",db="test")
cur = db.cursor()
#LENGTH = 450
#RESPONSE = 200
#OFFSETMAX = 45
#WEIGHT = [0.29,1,0.42,0.973,0.255]
WEIGHT = [1,1,1,1,1]
LENGTH = 250
RESPONSE = 250
OFFSETMAX = 40
trailnum = 9
for RESPONSE in range(200,500,50):
	for end in range(500,750,50):
		LENGTH = end - RESPONSE
		if LENGTH < 100:
			continue
		for OFFSETMAX in range(30,60,5):
			if LENGTH<OFFSETMAX*2:
				continue
			xiaoyanRAW = [[]] * trailnum
			jingweiRAW = [[]] * trailnum
			williamRAW = [[]] * trailnum
			aliRAW = [[]] * trailnum

			cur.execute("select theta,alpha,low_beta,high_beta,gamma from eeg_avg where person = 'Xiaoyan' order by time asc")
			xiaoyanAVG = np.asarray(cur.fetchall())

			cur.execute("select theta,alpha,low_beta,high_beta,gamma from eeg_avg where person = 'Jingwei' order by time asc")
			jingweiAVG = np.asarray(cur.fetchall())

			cur.execute("select theta,alpha,low_beta,high_beta,gamma from eeg_avg where person = 'William' order by time asc")
			williamAVG = np.asarray(cur.fetchall())

			cur.execute("select theta,alpha,low_beta,high_beta,gamma from eeg_avg where person = 'Ali' order by time asc")
			aliAVG = np.asarray(cur.fetchall())


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
			avgEEGDict = {'ali':aliAVG,'jingwei':jingweiAVG,'william':williamAVG,'xiaoyan':xiaoyanAVG}


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
						#ofile.write(message)
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
					#ofile.write("\n")
				#ofile.write("\n")
			#ofile.close()
			accuracy = correctTest/float(total)
			print("RESPONSE: "+str(RESPONSE)+" LENGTH: "+str(LENGTH)+" OFFSETMAX: "+str(OFFSETMAX))
			print("The accuracy is: "+str(accuracy))