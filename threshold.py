from model import *
import csv
path="C:\\Users\\mrhaboon\\Desktop\\seniorproject\\test_graphs\\"

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
	avgs=[]
	for i in range(4):
		avgs[i].append(full[i][time_index(full[i])][0])
	for i in range(4):
		avgs[i].append(av_of_waves(full[i]))
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
		if time>len(i[0])-1:
			time=len(i[0])-1
			index=i
	return index






def av_of_waves(trials):
	avg_trials=[["theta"],["alpha"],["low_beta"],["high_beta"],["gamma"]]

	return avg_trials




def indiv_wave(time, wave):
	wave1=[]
	for i in range(time):
		wave1.append((float(wave[0][time)+float(wave[1][time])+float(wave[2][time]))/3)
	return wave1
