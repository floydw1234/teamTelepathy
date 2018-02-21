from model import *

datab=[]
average_of_e=[]
tmp_rating=20*10^20
index=0

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

def av_of_all:

			

	
