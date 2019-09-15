from csv import *
from hashlib import *

filePath = "example.csv"



fileOpen = open(filePath, 'r')
 

fileReader = reader(fileOpen,)


storeHash = []


for row in fileReader :

	for tnx in row :

		currentItem = str(tnx)
		storeHash.append(sha256(currentItem.encode('utf-8')).hexdigest())



if (len(storeHash) % 2 != 0) :
	storeHash.append(storeHash[-1])


while (len(storeHash)> 1) : 
	

	j = 0;

	for i in range(0, len(storeHash) - 1) : 

		storeHash[j] = sha256(str(storeHash[i] + storeHash[i+1]).encode('utf-8')).hexdigest()
		
		i += 2
		j += 1


	lastDelete = i - j;

	del storeHash[-lastDelete:];


merkleFile = open('merkle.csv', 'w')


write = writer(merkleFile)

write.writerow(storeHash)
