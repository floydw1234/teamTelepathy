from model import *
import csv
#path="/home/ali/telep/test_graphs/"
path="C:\\Users\\mrhaboon\\Desktop\\seniorproject\\test_graphs\\"
#make a function for average given the database is the previous avg and new input
#avg keys will be 350-500 input will be full
#write script for old data

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

def transposewaves(full):
	full1=[]
	lent=0
	dblen=len(full)
	for i in range(len(full1)):
		avgs.append([])
	for i in range(dblen):
		lent=len(full[i])
		for x in range(lent):
			full1[i].append(m_inv1(full[i][x]))
	return full1

def untransposewaves(full):
	full1=[]
	lent=0
	dblen=len(full)
	for i in range(len(full1)):
		avgs.append([])
	for i in range(dblen):
		lent=len(full[i])
		for x in range(lent):
			full1[i].append(re_inv1(full[i][x]))
	return full1



def av_of_all(full1):
	full=transposewave(full1)
	avgs=[]
	dblen=len(full)
	for i in range(len(full)):
		avgs.append([])
	for i in range(dblen):
		avgs[i].append(full[i][time_index(full[i])][0])
	for i in range(dblen):
		avgs[i].extend(av_of_waves(full[i]))
		avgs[i].extend(get_tn(full[i]))
	#result=
	for i in range(len(avgs)):
		for x in range(8):
			
	return untransposewaves(avgs)

def get_tn(wave):
	result=[[],[]]
	result[0].extend(wave[-1][6])
	result[1].extend(wave[-1][7])
	return	result
		


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
			tmp.append(trials[x][i+1])
		avg_trials[i].extend(indiv_wave(time,tmp))

	return avg_trials




def indiv_wave(time, wave):
	wave1=[]
	for i in range(time):
		wave1.append((float(wave[0][i+1])+float(wave[1][i+1])+float(wave[2][i+1]))/3)
	return wave1

"""
final_result=av_of_all(datab1)
final_result1=re_inv(final_result[1])

with open('persons.csv', 'wb') as csvfile:
	filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	filewriter.writerow(final_result[1][0])
	filewriter.writerow(final_result[1][1])
	filewriter.writerow(final_result[1][2])
	filewriter.writerow(final_result[1][3])
	filewriter.writerow(final_result[1][4])
	filewriter.writerow(final_result[1][5])

with open('persons1.csv', 'wb') as csvfile:
	filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for i in final_result1:
		filewriter.writerow(i)




final_result1=[[],[],[],[]]

for i in range(4):
	for x in range(3):
		final_result1[i].append(m_inv(final_result[i][x]))"""










def new_avg(new, avg_key1):
	avg_key=m_inv1(avg_key1)
	weight=avg_key[6][1]
	for i in range(150):
		avg_key[6][1+i]=weight+1
	result=[avg_key[0],["theta"],["alpha"],["low_beta"],["high_beta"],["gamma"],avg_key[6],avg_key[7]]
	adj_new=m_inv1(new)
	for i in range(5):
		result[i+1].extend(avg_wave(adj_new[i+1][350:500],avg_key[i+1],weight))
	result1=re_inv1(in_mat)
	return result1







def avg_wave(wn,ww,weight):
	result=[]
	for i in range(150):
		result.append((wn+ww*weight)/2)
	return result
