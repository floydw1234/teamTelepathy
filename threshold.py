from model import *
import csv
path="/home/ali/telep/test_graphs"

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
	datab[0].append(open_csv('raw_eegAli-'+i+'.csv'))
	datab[1].append(open_csv('raw_eegJingwei-'+i+'.csv'))
	datab[2].append(open_csv('raw_eegXiaoyan-'+i+'.csv'))
	datab[3].append(open_csv('raw_eegWilliam-'+i+'.csv'))

for i in range(4):
	for x in range(3):
		datab1[i].append(m_inv(datab[i][x]))


def find_rating(ind,averages):
	for i in averages:
		tmp1=difference_rating(ind,i)
		if(abs(tmp_rating)>abs(tmp1)):
			tmp_rating=tmp1
	return tmp_rating					

		



def threshold(full):
	threshd=0
	for person in full:
		for t in person:
			tmp=find_rating(t,average_of_e)
			if threshd<tmp:
				threshd=tmp
	return threshd


def av_of_all(full):
	avgs=[[],[],[],[]]
	for i in range(4):
		if(len(full[i][0][0])<len(full[i][1][0])&&<len(full[i][2][0])):
			avgs[i].append(full[i][0][0])	
		elif(len(full[i][1][0])<len(full[i][2][0])):
			avgs[i].append(full[i][1][0])	
		else:
			avgs[i].append(full[i][2][0])	
	for i in range(4):
		avgs[i].append(av_of_waves([]))

	return avgs
		



def av_of_waves(wave):
	time=len(wave[0])-1
	agg_wave=[wave[0][0],[]]
	for i in range(3):
		if time>len(wave[i])-1:
			time=len(wave[i])-1
	for i in range(time):
		agg_wave[1].append((float(wave[0][time+1])+float(wave[1][time+1])+float(wave[2][time+1]))/3)
	return agg_wave
		

	

	
