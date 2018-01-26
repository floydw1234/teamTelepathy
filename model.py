

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
       			rating+=float(in_sorted[wave][t])-float(pass_sorted[wave][t])
	
	return rating


def avg_rating(infinger_print,passfinger_print):


	rating=0

	in_sorted=m_inv(infinger_print)
	pass_sorted=m_inv(passfinger_print)
	
	avg_in=avgof_mat(in_sorted)
	avg_pass=avgof_mat(pass_sorted)
	
	rating=avg_in-avg_pass
	
	return rating


    


def m_inv(in_mat):

	theta=[]
	alpha=[]
	low_beta=[]
	high_beta=[]
	gamma=[]

	for row in in_mat[1:]: #this is to change the input array from wave x time to time x wave
		theta.append(row[1])
   	 	alpha.append(row[2])
  	  	low_beta.append(row[3])
  		high_beta.append(row[4])
  		gamma.append(row[5])

	brainwave=[theta,alpha,low_beta,high_beta,gamma]

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
    


