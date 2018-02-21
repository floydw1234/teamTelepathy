from model import *
import csv
path='/home/mrhaboon/teamTelepathy/test_graphs/'



def open_csv(in_csv):
	with open(path+in_csv,"rb") as f:
    		reader = csv.reader(f)
	    	user = list(reader)
	return user

ali=open_csv('Ali_raw_eeg.csv')
jenny=open_csv('Jenny_raw_eeg.csv')
angela=open_csv('Angela_raw_eeg.csv')
will=open_csv('will_raw_eeg.csv')


listofusers=[ali,jenny,angela,will]

test=open_csv('Ali_2_raw_eeg.csv')

tmp_rating=20*10^20
index=0

for i in listofusers:
	tmp1=difference_rating(test,i)
	if(abs(tmp_rating)>abs(tmp1)):
		tmp_rating=tmp1
		index=listofusers.index(i)
		


print(index)

	
