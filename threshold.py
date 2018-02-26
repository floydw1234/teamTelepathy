from model import *
import csv
path="/home/ali/telep/test_graphs/"
#make a function for average given the database is the previous avg and new input
#avg keys will be 350-500 input will be full

datab=[[],[],[],[]]
datab1=[[],[],[],[]]

average_of_e=[]
tmp_rating=20*10^20
index=0

def open_csv(in_csv):
	with open(path+in_csv,"rb") as f:
    		reader = csv.reader(f)
	    	user = list(reader)
	return user

for i in range(3):
	datab[0].append(open_csv('raw_eegAli-'+str(i)+'.csv'))
	datab[1].append(open_csv('raw_eegJingwei-'+str(i)+'.csv'))
	datab[2].append(open_csv('raw_eegXiaoyan-'+str(i)+'.csv'))
	datab[3].append(open_csv('raw_eegWilliam-'+str(i)+'.csv'))

for i in range(4):
	for x in range(3):
		datab1[i].append(m_inv(datab[i][x]))


	

def av_of_all(full):
	avgs=[[],[],[],[]]
	for i in range(4):
		avgs[i].append(full[i][time_index(full[i])][0])
	for i in range(4):
		avgs[i].extend(av_of_waves(full[i]))
	return avgs




def least_time(trials):
	time=len(trials[0][0])-1
	for i in trials:
		if time>len(i[0])-1:
			time=len(i[0])-1
	return time

def time_index(trials):
	index=0
	time=len(trials[0][0])-1
	for i in range(len(trials)):
		if time>len(trials[i][0])-1:
			time=len(trials[i][0])-1
			index=i
	return index






def av_of_waves(trials):
	avg_trials=[["theta"],["alpha"],["low_beta"],["high_beta"],["gamma"]]
	time=least_time(trials)
	for i in range(5):
		tmp=[]
		for x in range(len(trials)):
			tmp.append(trials[x][i])
		print(len(tmp[0]))
		avg_trials[i].extend(indiv_wave(time,tmp))
		
	return avg_trials




def indiv_wave(time, wave):
	wave1=[]
	for i in range(time):
		wave1.append((float(wave[0][time])+float(wave[1][time])+float(wave[2][time]))/3)
	return wave1


final_result=av_of_all(datab1)

print(final_result[0][3][0])

with open('persons.csv', 'wb') as csvfile:
	filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	filewriter.writerow(final_result[0][0])
	filewriter.writerow(final_result[0][1])	
	filewriter.writerow(final_result[0][2])
	filewriter.writerow(final_result[0][3])
	filewriter.writerow(final_result[0][4])
	filewriter.writerow(final_result[0][5])

	
"""
final_result1=[[],[],[],[]]

for i in range(4):
	for x in range(3):
		final_result1[i].append(m_inv(final_result[i][x]))"""


