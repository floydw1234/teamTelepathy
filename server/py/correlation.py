import numpy as np

LENGTH = 150
RESPONSE = 350
OFFSETMAX = 40
CHANNEL = 5


def getCorrelationLeft(raw_eeg,avg_eeg,idx):
    theta = raw_eeg[:,0:1].T[0][idx:]
    alpha = raw_eeg[:,1:2].T[0][idx:]
    low_beta = raw_eeg[:,2:3].T[0][idx:]
    high_beta = raw_eeg[:,3:4].T[0][idx:]
    gamma = raw_eeg[:,4:5].T[0][idx:]
    t_avg = avg_eeg[:,0:1].T[0][:LENGTH-idx]
    a_avg = avg_eeg[:,1:2].T[0][:LENGTH-idx]
    lb_avg = avg_eeg[:,2:3].T[0][:LENGTH-idx]
    hb_avg = avg_eeg[:,3:4].T[0][:LENGTH-idx]	
    g_avg = avg_eeg[:,4:5].T[0][:LENGTH-idx]
    return (abs(np.corrcoef(theta,t_avg)[0][1]),abs(np.corrcoef(alpha,a_avg)[0][1]),abs(np.corrcoef(low_beta,lb_avg)[0][1]),abs(np.corrcoef(high_beta,hb_avg)[0][1]),abs(np.corrcoef(gamma,g_avg)[0][1]))
def getCorrelationRight(raw_eeg,avg_eeg,idx):
    theta = raw_eeg[:,0:1].T[0][:LENGTH-idx]
    alpha = raw_eeg[:,1:2].T[0][:LENGTH-idx]
    low_beta = raw_eeg[:,2:3].T[0][:LENGTH-idx]
    high_beta = raw_eeg[:,3:4].T[0][:LENGTH-idx]
    gamma = raw_eeg[:,4:5].T[0][:LENGTH-idx]
    t_avg = avg_eeg[:,0:1].T[0][idx:]
    a_avg = avg_eeg[:,1:2].T[0][idx:]
    lb_avg = avg_eeg[:,2:3].T[0][idx:]
    hb_avg = avg_eeg[:,3:4].T[0][idx:]
    g_avg = avg_eeg[:,4:5].T[0][idx:]
    return (abs(np.corrcoef(theta,t_avg)[0][1]),abs(np.corrcoef(alpha,a_avg)[0][1]),abs(np.corrcoef(low_beta,lb_avg)[0][1]),abs(np.corrcoef(high_beta,hb_avg)[0][1]),abs(np.corrcoef(gamma,g_avg)[0][1]))
def maxCorrelation(data,avg_eeg):
    result = []
    #truncate raw data[350:500] into raw_eeg
    #RESPONSE: is the start sample for response
    raw_eeg= data[RESPONSE:RESPONSE+LENGTH,:]
    
    #find max correlation shift index
    sum_max = []
    index = []
    
    for idx in range(OFFSETMAX):
		sum_tuple = getCorrelationLeft(raw_eeg,avg_eeg,idx)
		sum = 0
		for i in range(CHANNEL):
			sum += sum_tuple[i].item(0)
		sum_max.append(sum)
		index.append(-idx)
  
    for idx in range(OFFSETMAX):
		sum_tuple = getCorrelationRight(raw_eeg,avg_eeg,idx)
		sum = 0 
		for i in range(CHANNEL):
			sum += sum_tuple[i].item(0)
		sum_max.append(sum)
		index.append(idx)
	
    max_idx = np.argmax(sum_max)
    max_shift_idx = index[max_idx]
    #get max correlation for theta, alpha, low_beta, high_beta, gamma(assume this order)
    cor_max = []
    if max_shift_idx < 0:
        cor_tuple = getCorrelationLeft(raw_eeg,avg_eeg,max_idx)
    else:
        cor_tuple = getCorrelationRight(raw_eeg,avg_eeg,max_idx)
    for i in range(CHANNEL):
        cor_max.append(round(cor_tuple[i].item(0),2))
    
    #append 
    result.append(cor_max)
    result.append(max_shift_idx)
    return result