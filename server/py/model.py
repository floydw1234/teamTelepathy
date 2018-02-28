"change difference to correlation multiple alpha by 1.1"
#threshold finalize

def difference_rating(infinger_print,passfinger_print):
	time1=len(infinger_print)-1
	time2=len(passfinger_print)-1
	time=0

	if time1<time2:
		time=time1
	else:
		time=time2


	rating=0

	in_sorted=m_inv(infinger_print)
	pass_sorted=m_inv(passfinger_print)


	for wave in range(5):
   		for t in range(time):
       			rating+=float(in_sorted[wave+1][t+1])-float(pass_sorted[wave+1][t+1])

	return rating


def avg_rating(infinger_print,passfinger_print):


	rating=0

	in_sorted=m_inv(infinger_print)
	pass_sorted=m_inv(passfinger_print)

	avg_in=avgof_mat(in_sorted)
	avg_pass=avgof_mat(pass_sorted)

	rating=avg_in-avg_pass

	return rating


def m_inv1(in_mat):
	time=[]
	theta=[]
	alpha=[]
	low_beta=[]
	high_beta=[]
	gamma=[]
	trials=[]
	name=[]

	for row in in_mat: #this is to change the input array from wave x time to time x wave
		time.append(row[0])
		theta.append(row[1])
   	 	alpha.append(row[2])
  	  	low_beta.append(row[3])
  		high_beta.append(row[4])
  		gamma.append(row[5])
		trials.append(row[6])
		name.append(row[7])

	brainwave=[time,theta,alpha,low_beta,high_beta,gamma,trials,name]

	return brainwave

def re_inv1(in_mat):
	mlen=len(in_mat[0])
	result=[]
	result.append(["time","theta","alpha","low_beta","high_beta","gamma","trials","name"])
	for i in range(mlen):
		tmp=[]
		for x in range(8):
			tmp.append(in_mat[x][i])
		result.append(tmp)
	return result

def re_inv(in_mat):
	mlen=len(in_mat[0])-1
	result=[]
	result.append(["time","theta","alpha","low_beta","high_beta","gamma"])
	for i in range(mlen):
		tmp=[]
		for x in range(6):
			tmp.append(in_mat[x][i+1])
		result.append(tmp)
	return result


def m_inv(in_mat):
	time=["time"]
	theta=["theta"]
	alpha=["alpha"]
	low_beta=["low_beta"]
	high_beta=["high_beta"]
	gamma=["gamma"]

	for row in in_mat[1:]: #this is to change the input array from wave x time to time x wave
		time.append(row[0])
		theta.append(row[1])
   	 	alpha.append(row[2])
  	  	low_beta.append(row[3])
  		high_beta.append(row[4])
  		gamma.append(row[5])

	brainwave=[time,theta,alpha,low_beta,high_beta,gamma]

	return brainwave


def avgof_mat(in_mat):
	avg_in=0
	for i in in_mat:
		tmp=0
		for entry in i:
			tmp+=float(entry)
		tmp=tmp/len(i)
		avg_in+=tmp

	return avg_in



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
