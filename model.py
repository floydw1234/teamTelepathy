import csv
with open('ES.csv') as f:
    reader = csv.reader(f)
    testinguser = list(reader)

password=[,,,,]


time=len(testinguser)-1
print(time)

rating=0

theta=[]
alpha=[]
low_beta=[]
high_beta=[]
gamma=[]


for row in testinguser[1:]: #this is to change the input array from wave x time to time x wave
    theta.append(row[1])
    alpha.append(row[2])
    low_beta.append(row[3])
    high_beta.append(row[4])
    gamma.append(row[5])

brainwave=[theta,alpha,low_beta,high_beta,gamma]


for wave in range(5):
    for t in range(time):
        rating+=testinguser[wave][t]-password[wave][t]




    



    


